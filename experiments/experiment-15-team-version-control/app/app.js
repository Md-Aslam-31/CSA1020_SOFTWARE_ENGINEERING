const modules=[
  {code:"CAT",name:"Campus Directory",description:"Search buildings, services, and accessible campus routes.",owner:"Directory team",branch:"feature/directory",status:"In review"},
  {code:"EVT",name:"Events & Clubs",description:"Discover student groups and reserve a place at campus events.",owner:"Community team",branch:"feature/events",status:"In progress"},
  {code:"SUP",name:"Student Support",description:"Find wellbeing contacts and support options by topic.",owner:"Support team",branch:"feature/support",status:"In progress"}
];
const grid=document.querySelector('#modules');
function render(query=''){
  const shown=modules.filter(module=>`${module.code} ${module.name} ${module.description} ${module.owner}`.toLowerCase().includes(query.toLowerCase()));
  grid.replaceChildren(...shown.map(module=>{
    const card=document.createElement('article');card.className='module';
    const head=document.createElement('div');head.className='module-head';
    const icon=document.createElement('span');icon.className='module-icon';icon.textContent=module.code;
    const status=document.createElement('span');status.className='status';status.textContent=module.status;
    head.append(icon,status);
    const title=document.createElement('h3');title.textContent=module.name;
    const description=document.createElement('p');description.textContent=module.description;
    const owner=document.createElement('div');owner.className='owner';
    const ownerName=document.createElement('strong');ownerName.textContent=module.owner;
    const branch=document.createElement('span');branch.textContent=module.branch;
    owner.append(ownerName,branch);card.append(head,title,description,owner);return card;
  }));
  if(!shown.length){const empty=document.createElement('p');empty.textContent='No modules match that search.';grid.append(empty)}
}
document.querySelector('#search').addEventListener('input',event=>render(event.target.value));
render();
