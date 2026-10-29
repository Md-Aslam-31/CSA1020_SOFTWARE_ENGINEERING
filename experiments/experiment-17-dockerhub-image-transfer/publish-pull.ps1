param([Parameter(Mandatory=$true)][string]$DockerHubUser)
$ErrorActionPreference='Stop'
$previousLocation = Get-Location
Set-Location $PSScriptRoot
$image="$DockerHubUser/campusconnect:1.0"
try {
    docker build -t $image .
    if($LASTEXITCODE -ne 0){throw 'Docker build failed'}
    docker login --username $DockerHubUser
    if($LASTEXITCODE -ne 0){throw 'Docker login failed'}
    docker push $image
    if($LASTEXITCODE -ne 0){throw 'Docker push failed'}
    docker pull $image
    if($LASTEXITCODE -ne 0){throw 'Docker pull failed'}
    docker run --rm -d --name campusconnect-pulled -p 8081:80 $image
    if($LASTEXITCODE -ne 0){throw 'Docker run failed'}
    Write-Host 'Verify http://localhost:8081 then stop campusconnect-pulled with: docker stop campusconnect-pulled'
}
finally {
    Set-Location $previousLocation
}
