let button = document.querySelector('#button')
    button.addEventListener('click', fn)

let main = document.querySelector('#main')
function fn() {
    main.innerHTML=''
    fetch('https://deniszk.pythonanywhere.com/api/v1/products/')
        .then(resp=>resp.json())
        .then(data=>{
            console.log(data)
            data.map(item=>{
                main.innerHTML+=`<div class="card">
                                    <p>${item.title}</p>
                                    <p>${item.price}</p>
                                    <img style="max-width: 100px" src="${item.image}" alt="${item.image}">
                                </div>`
            })
        })

    setInterval(()=>{
            main.innerHTML=''
    fetch('https://deniszk.pythonanywhere.com/api/v1/products/')
        .then(resp=>resp.json())
        .then(data=>{
            console.log(data)
            data.map(item=>{
                main.innerHTML+=`<div class="card">
                                    <p>${item.title}</p>
                                    <p>${item.price}</p>
                                    <img style="max-width: 100px" src="${item.image}" alt="${item.image}">

                                    
                                </div>`
            })
        })
    }, 1000)
}