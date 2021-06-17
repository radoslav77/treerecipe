const data = document.querySelector('.recipe')
let dataText = []
const i = data.innerText.split('\n')
const btns = document.querySelectorAll('button') 

btns.forEach((btn) => {

   btn.addEventListener('click', ()=>{
           const times = btn.value
           console.log(times)
       if (times === '1') {
           window.location.reload(true)
           return false
       } else {
           i.forEach((e) => {
               var num = e.split(/\s+/)

               num.forEach((b) => {
                   if(isNaN(b)){

                   } else {
                   let c = b * times
                   const tmp = num[0]
                   num[0] = Math.floor(c)
                                           
                   }
                   
                   
               })
                       e = num
                       const tmp = e.join(' ')
                       
                       //console.log(tmp)
                       const li = document.createElement('li')
                       const original = document.querySelector('.original')
                      // const linkOriginal = document.getElementById('original')
                       li.style.display = 'block'
                       dataText.push(li)
                       if (tmp === '0') {
                           li.innerHTML = ''
                           
                       } else  {
                           
                           
                           
                           original.style.display = 'none'
                          // linkOriginal.style.display = 'none'
                           document.getElementById('title').style.display = 'none'

                           li.innerHTML =`${tmp}`
                           console.log(tmp[0][0])
                       }
                       data.appendChild(li)
                       document.querySelector('.times-x').style.display = 'none'
                       document.getElementById('reload').style.display = 'block'

       })}

   })
   
})

