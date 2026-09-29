var itemsCount = 3;
var intialPrice = 15097
var finalPrice
var cartItem = 1;

const products = {

    
    "Suzuki Streeing" : "Suzuki Steering systems are known for their precision and reliability, offering superior handling and comfort for drivers. With a focus on innovation and advanced technology, Suzuki steering mechanisms are designed to provide a smooth and responsive driving experience. Whether it's power steering or electronic steering, Suzuki ensures that every vehicle is equipped with an easy-to-use, durable, and efficient steering system to enhance overall performance and safety on the road.",
    "Infotainment System" : "Infotainment System in modern vehicles provides a seamless integration of entertainment, navigation, and connectivity features. It allows drivers and passengers to enjoy music, movies, apps, and GPS navigation with ease. With features like touchscreens, voice control, and smartphone connectivity, the infotainment system enhances the driving experience by keeping drivers informed, entertained, and connected, all while minimizing distractions on the road.",
    "Suzuki Gear Knob" : "Suzuki Gear Knob is designed to provide a smooth and ergonomic shifting experience for drivers. Crafted with precision and durability, it offers a comfortable grip, allowing for easy and responsive gear changes. Whether it's a manual or automatic transmission, Suzuki’s gear knobs are designed to enhance the vehicle’s interior aesthetics while improving the overall driving experience with their functional and stylish design."
}
const navMenu = document.getElementById('nav-menu'),
      navToggle = document.getElementById('nav-toggle'),
      navClose = document.getElementById('nav-close')
if(navToggle){
    navToggle.addEventListener('click', () =>{
        navMenu.classList.add('show-menu')
    })
}
if(navClose){
    navClose.addEventListener('click', () =>{
        navMenu.classList.remove('show-menu')
    })
}
const navLink = document.querySelectorAll('.nav__link')
const linkAction = () =>{
    const navMenu = document.getElementById('nav-menu')
    navMenu.classList.remove('show-menu')
}
navLink.forEach(n => n.addEventListener('click', linkAction))
const scrollHeader = () =>{
    const header = document.getElementById('header')
    this.scrollY >= 50 ? header.classList.add('scroll-header') 
                       : header.classList.remove('scroll-header')
}
window.addEventListener('scroll', scrollHeader)
let testimonialSwiper = new Swiper(".testimonial-swiper", {
    spaceBetween: 30,
    loop: 'true',

    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
});
let newSwiper = new Swiper(".new-swiper", {
    spaceBetween: 24,
    loop: 'true',

    breakpoints: {
        576: {
          slidesPerView: 2,
        },
        768: {
          slidesPerView: 3,
        },
        1024: {
          slidesPerView: 4,
        },
    },
});
const sections = document.querySelectorAll('section[id]')
const scrollActive = () =>{
  	const scrollDown = window.scrollY
	sections.forEach(current =>{
		const sectionHeight = current.offsetHeight,
			  sectionTop = current.offsetTop - 58,
			  sectionId = current.getAttribute('id'),
			  sectionsClass = document.querySelector('.nav__menu a[href*=' + sectionId + ']')

		if(scrollDown > sectionTop && scrollDown <= sectionTop + sectionHeight){
			sectionsClass.classList.add('active-link')
		}else{
			sectionsClass.classList.remove('active-link')
		}                                                    
	})
}

function handleDelete(icon){

    const container = icon.closest('.cart__card')
    let price = container.querySelector('.cart__price')
    price = price.innerHTML
    price = Number.parseInt(price.replace("Rs.",""),10)
    finalPrice = intialPrice - price
    container.style.display = 'none'
   
    if(itemsCount > 0){

        itemsCount -- ;
        UpdateCartItems()
    }
    
}

function handlePlus(icon){

    let parentContainer = icon.closest('.cart__amount-content')
    let itemCount = parentContainer.querySelector('.cart__amount-number')
    let cartDetails = icon.closest('.cart__details')
    let itemPrice = cartDetails.querySelector('.cart__price')
    itemPrice = itemPrice.innerHTML
    itemPrice = Number.parseInt(itemPrice.replace("Rs.",""),10)
    cartItem = itemCount.innerHTML
    cartItem ++
    itemCount.innerHTML = cartItem

    updateTotalPrice(itemPrice,cartItem)

}

function handleMinus(icon){

    let parentContainer = icon.closest('.cart__amount-content')
    let itemCount = parentContainer.querySelector('.cart__amount-number')
    let newCount = itemCount.innerHTML
    newCount--
    itemCount.innerHTML = newCount

}

function handleDescription(icon){

    let container = icon.closest('.featured__card')
    let itemHeading = container.querySelector('.featured__title')
    console.log('itemHeading-->'+itemHeading.innerHTML)
    let modalOverlay = document.querySelector('.modal-overlay');
    let modalHeader = document.querySelector('.modal-header')
    let modalBody = document.querySelector('.modal-body')
    modalHeader.innerHTML = itemHeading.innerHTML
    modalBody.innerHTML = products[itemHeading.innerHTML]
    modalOverlay.style.display = 'block';
    
}

function handleClose(){
    let modalOverlay = document.querySelector('.modal-overlay');
    let closeModalBtn = document.querySelector('.close-btn');
    modalOverlay.style.display = 'none'

}

function UpdateCartItems(){
if(itemsCount > 0){
    const element = document.querySelector('.cart__prices-item')
    const totalPrice = document.querySelector('.cart__prices-total')
    totalPrice.innerHTML = ` Rs. ${finalPrice}`
    element.innerHTML = `${itemsCount} items`

}
else{
     const element = document.querySelector('.cart__prices-item')
    element.innerHTML = ''
    const totalPrice = document.querySelector('.cart__prices-total')
    totalPrice.style.display = 'none'
    
}
}

function updateTotalPrice(itemPrice,itemCount){

let totalItem = itemCount - 1; // as intially one item is already added to the total price 
let priceOfItem = itemPrice

let totalPrice = intialPrice + (totalItem*priceOfItem)

    const totalPriceSelector = document.querySelector('.cart__prices-total')
    totalPriceSelector.innerHTML = ` Rs. ${totalPrice}`

}
window.addEventListener('scroll', scrollActive)
const scrollUp = () =>{
	const scrollUp = document.getElementById('scroll-up')
	this.scrollY >= 350 ? scrollUp.classList.add('show-scroll')
						: scrollUp.classList.remove('show-scroll')
}
window.addEventListener('scroll', scrollUp)
const cart = document.getElementById('cart'),
      cartShop = document.getElementById('cart-shop'),
      cartClose = document.getElementById('cart-close')

if(cartShop){
    cartShop.addEventListener('click', () =>{
        cart.classList.add('show-cart')
    })
}
if(cartClose){
    cartClose.addEventListener('click', () =>{
        cart.classList.remove('show-cart')
    })
}
const themeButton = document.getElementById('theme-button')
const darkTheme = 'dark-theme'
const iconTheme = 'bx-sun'
const selectedTheme = localStorage.getItem('selected-theme')
const selectedIcon = localStorage.getItem('selected-icon')
const getCurrentTheme = () => document.body.classList.contains(darkTheme) ? 'dark' : 'light'
const getCurrentIcon = () => themeButton.classList.contains(iconTheme) ? 'bx bx-moon' : 'bx bx-sun'
if (selectedTheme) {
  document.body.classList[selectedTheme === 'dark' ? 'add' : 'remove'](darkTheme)
  themeButton.classList[selectedIcon === 'bx bx-moon' ? 'add' : 'remove'](iconTheme)
}


themeButton.addEventListener('click', () => {
    document.body.classList.toggle(darkTheme)
    themeButton.classList.toggle(iconTheme)
    localStorage.setItem('selected-theme', getCurrentTheme())
    localStorage.setItem('selected-icon', getCurrentIcon())
})
