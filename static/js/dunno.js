// let slideUp = (e, t = 500) => {
//     e.style.transitionProperty = "height, margin, padding",
//     e.style.transitionDuration = t + "ms",
//     e.style.boxSizing = "border-box",
//     e.style.height = e.offsetHeight + "px", e.offsetHeight,
//     e.style.overflow = "hidden",
//     e.style.height = 0,
//     e.style.paddingTop = 0,
//     e.style.paddingBottom = 0,
//     e.style.marginTop = 0,
//     e.style.marginBottom = 0,
//     window.setTimeout(() => {
//         e.style.display = "none",
//         e.style.removeProperty("height"),
//         e.style.removeProperty("padding-top"),
//         e.style.removeProperty("padding-bottom"),
//         e.style.removeProperty("margin-top"),
//         e.style.removeProperty("margin-bottom"),
//         e.style.removeProperty("overflow"),
//         e.style.removeProperty("transition-duration"),
//         e.style.removeProperty("transition-property")
//     }, t)
// },
// slideDown = (e, t = 500) => {
//     e.style.removeProperty("display");
//     let o = window.getComputedStyle(e).display;
//     "none" === o && (o = "block"), e.style.display = o;
//     var a = e.offsetHeight;
//     e.style.overflow = "hidden",
//     e.style.height = 0,
//     e.style.paddingTop = 0,
//     e.style.paddingBottom = 0,
//     e.style.marginTop = 0,
//     e.style.marginBottom = 0,
//     e.offsetHeight,
//     e.style.boxSizing = "border-box",
//     e.style.transitionProperty = "height, margin, padding",
//     e.style.transitionDuration = t + "ms",
//     e.style.height = a + "px",
//     e.style.removeProperty("padding-top"),
//     e.style.removeProperty("padding-bottom"),
//     e.style.removeProperty("margin-top"),
//     e.style.removeProperty("margin-bottom"),
//     window.setTimeout(() => {
//         e.style.removeProperty("height"),
//         e.style.removeProperty("overflow"),
//         e.style.removeProperty("transition-duration"),
//         e.style.removeProperty("transition-property")
//     }, t)
// },
// slideToggle = (e, t = 500) => ("none" === window.getComputedStyle(e).display ? slideDown : slideUp)(e, t),
// scrollpos = window.scrollY;
// const header = document.querySelector(".site-header"),
// $win = $(window);
// let windowHeight = $win.height();
// window.addEventListener("scroll", () => {
//     scrollpos = window.scrollY, 0 < scrollpos ? header.classList.add("site-header--fixed") : header.classList.remove("site-header--fixed"), $(".page-home .site-header").length && ($(window).scrollTop() > windowHeight - $(".site-header").height() ? $(".page-home .site-header").addClass("site-header--opaque") : $(".page-home .site-header").removeClass("site-header--opaque"))
// });
// const navToggle = document.querySelector(".site-nav__toggle"),
// nav = document.querySelector(".site-nav > ul");
// navToggle.addEventListener("click", () => {
//     document.querySelector(".site-header").classList.toggle("site-header--menu-open"), 
//     navToggle.classList.toggle("is-active"),
//     slideToggle(nav, 200)
// }), window.addEventListener("scroll", () => {
//     navToggle.classList.remove("is-active"),
//     document.querySelector(".site-header").classList.remove("site-header--menu-open"),
//     slideUp(nav, 200)
// });

