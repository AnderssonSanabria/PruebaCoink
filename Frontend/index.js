function setUsers() {
    let url = 'http://localhost:8081';
    const res = fetch(`${url}/users`,{method:'POST',headers:{'Content-Type':'application/json',}, body:SetFormUsers()})
    .then( response => response.json() )
    .then( users => console.log(users))
    .catch( error => console.log(error) )
  }


function SetFormUsers(){
    const form = document.getElementById('formUser')
    let userForm = new FormData(form);
    let user=JSON.stringify(Object.fromEntries(userForm));
    console.log(user)
    return user;
}
let content=document.querySelector('#conentTable');
function getUsers() {
    let url = 'http://localhost:8081';
    const res = fetch(`${url}/users`)
    .then( response => response.json() )
    .then( users => createTable(users))
    .catch( error => console.log(error) )
  }

function createTable(data){
    console.log(data);
    for (let iterator of data) {
        content.innerHTML +=`
        <tr>
            <th scope="col">${iterator.id}</th>
            <th scope="col">${iterator.email}</th>
            <th scope="col">${iterator.fullname}</th>
            <th scope="col">${iterator.city}</th>
        </tr>
        `  
    }
}
getUsers()