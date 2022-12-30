const NavsTab = document.querySelector('#nav-tab');
const Navs = NavsTab.querySelectorAll('button[data-bs-toggle="tab"]');

Navs.forEach(Nav => {
  Nav.addEventListener('shown.bs.tab', (event) => {
    const { target } = event;
    const { id: targetId } = target;
    
    saveNavId(targetId);
  });
});

const saveNavId = (selector) => {
  localStorage.setItem('activeNavId', selector);
};

const getNavId = () => {
  const activeNavId = localStorage.getItem('activeNavId');
  
  // if local storage item is null, show default tab
  if (!activeNavId) return;
  
  // call 'show' function
  const someTabTriggerEl = document.querySelector(`#${activeNavId}`)
  const tab = new bootstrap.Tab(someTabTriggerEl);

  tab.show();
};

// get Nav id on load
getNavId();