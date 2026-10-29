$ErrorActionPreference = 'Stop'
$labRoot = Join-Path ([IO.Path]::GetTempPath()) ("se-exp23-" + [guid]::NewGuid().ToString('N'))
$bare = Join-Path $labRoot 'shared.git'
$writer = Join-Path $labRoot 'writer'
$reader = Join-Path $labRoot 'reader'
$evidencePath = Join-Path $PSScriptRoot 'evidence\pull-verification.txt'
New-Item -ItemType Directory -Path $labRoot | Out-Null
New-Item -ItemType Directory -Path (Split-Path -Parent $evidencePath) -Force | Out-Null

function Invoke-Git([string]$Path, [string[]]$GitArgs) {
    & git -C $Path @GitArgs
    if ($LASTEXITCODE -ne 0) { throw "git $($GitArgs -join ' ') failed" }
}

try {
    & git init --bare --initial-branch=main $bare | Out-Null
    if ($LASTEXITCODE -ne 0) { throw 'Could not initialize the local shared remote' }
    & git clone $bare $writer | Out-Null
    if ($LASTEXITCODE -ne 0) { throw 'Could not clone the writer workspace' }
    Invoke-Git $writer @('config','user.name','Md-Aslam-31 (local lab)')
    Invoke-Git $writer @('config','user.email','experiment23@users.noreply.github.com')
    Set-Content -LiteralPath (Join-Path $writer 'README.md') -Value "# CampusConnect`n`nA campus-support planning prototype.`n"
    Invoke-Git $writer @('add','README.md')
    Invoke-Git $writer @('commit','-m','Create collaboration simulation baseline') | Out-Null
    Invoke-Git $writer @('push','-u','origin','main') | Out-Null

    & git clone $bare $reader | Out-Null
    if ($LASTEXITCODE -ne 0) { throw 'Could not clone the reader workspace' }
    Invoke-Git $reader @('config','user.name','Md-Aslam-31 (local lab)')
    Invoke-Git $reader @('config','user.email','experiment23@users.noreply.github.com')

    Add-Content -LiteralPath (Join-Path $writer 'README.md') -Value "Before editing, fetch or pull the latest shared change so the local copy is current."
    Invoke-Git $writer @('add','README.md')
    Invoke-Git $writer @('commit','-m','Document how to synchronize a shared clone') | Out-Null
    Invoke-Git $writer @('push','origin','main') | Out-Null
    Invoke-Git $reader @('pull','--ff-only','origin','main') | Out-Null

    $writerHead = (Invoke-Git $writer @('rev-parse','HEAD') | Out-String).Trim()
    $readerHead = (Invoke-Git $reader @('rev-parse','HEAD') | Out-String).Trim()
    $status = (Invoke-Git $reader @('status','--short') | Out-String).Trim()
    $readme = Get-Content -LiteralPath (Join-Path $reader 'README.md') -Raw
    if ($writerHead -ne $readerHead -or $status -ne '' -or $readme -notmatch 'fetch or pull') {
        throw 'Reader verification did not match the pushed update'
    }

    @(
        'Experiment 23 local two-clone simulation',
        "Writer HEAD: $writerHead",
        "Reader HEAD: $readerHead",
        'Reader working tree: clean',
        'Pulled README update: verified',
        'Remote type: local bare repository; no GitHub collaborator account was used.'
    ) | Set-Content -LiteralPath $evidencePath
    Get-Content -LiteralPath $evidencePath
}
finally {
    Remove-Item -LiteralPath $labRoot -Recurse -Force -ErrorAction SilentlyContinue
}
