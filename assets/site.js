const toggle=document.querySelector('.menu-toggle');
const menu=document.querySelector('.nav-links');
if(toggle&&menu){
 function closeMenu(){toggle.setAttribute('aria-expanded','false');menu.classList.remove('is-open');toggle.textContent='Menu';}
 toggle.addEventListener('click',()=>{const open=toggle.getAttribute('aria-expanded')!=='true';toggle.setAttribute('aria-expanded',String(open));menu.classList.toggle('is-open',open);toggle.textContent=open?'Close':'Menu';});
 menu.addEventListener('click',e=>{if(e.target.closest('a'))closeMenu();});
 document.addEventListener('keydown',e=>{if(e.key==='Escape'&&toggle.getAttribute('aria-expanded')==='true'){closeMenu();toggle.focus();}});
 document.addEventListener('click',e=>{if(!e.target.closest('.nav'))closeMenu();});
 matchMedia('(min-width: 801px)').addEventListener('change',e=>{if(e.matches)closeMenu();});
}
const copy=document.querySelector('[data-copy-email]');
if(copy)copy.addEventListener('click',async()=>{const status=document.querySelector('.copy-status');try{await navigator.clipboard.writeText('contact@solassovereignsystems.ai');status.textContent='Email address copied.';}catch{status.textContent='Select and copy the email address above, or use the email link.';}});
// Preserve links shared from the previous one-page site.
const legacy={services:'expertise.html',industries:'expertise.html#industries',platform:'platform.html',sovereignty:'approach.html',principles:'approach.html#principles',process:'approach.html#process',about:'about.html',join:'platform.html#collaborate',thinking:'resources.html',resources:'resources.html',faq:'contact.html#faq',research:'about.html#foundation',contact:'contact.html'};
if(document.body.dataset.page==='home'&&legacy[location.hash.slice(1)])location.replace(legacy[location.hash.slice(1)]);
