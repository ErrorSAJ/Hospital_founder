$(document).ready(function () {
  $(".fullpage-slider").slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: true,
    dots: true,
    infinite: true,
    speed: 800,
    autoplay: true,
    autoplaySpeed: 4000,
    fade: false,
    cssEase: "ease-in-out",
    adaptiveHeight: false,
    vertical: false,
  });

  // Keyboard navigation
  $(document).on("keydown", function (e) {
    if (e.keyCode === 38) {
      $(".fullpage-slider").slick("slickPrev");
    } else if (e.keyCode === 40) {
      $(".fullpage-slider").slick("slickNext");
    }
  });
});

// Burger Menu Toggle
const burger = document.getElementById("burger");
const menu = document.getElementById("menu");

burger.addEventListener("click", function () {
  this.classList.toggle("is-active");
  menu.classList.toggle("is-active");
});

// Close menu when clicking on a link
const menuLinks = document.querySelectorAll(".menu-link");
menuLinks.forEach((link) => {
  link.addEventListener("click", function () {
    burger.classList.remove("is-active");
    menu.classList.remove("is-active");
  });
});

// Close menu when clicking outside
document.addEventListener("click", function (event) {
  const isClickInsideMenu = menu.contains(event.target);
  const isClickOnBurger = burger.contains(event.target);

  if (
    !isClickInsideMenu &&
    !isClickOnBurger &&
    menu.classList.contains("is-active")
  ) {
    burger.classList.remove("is-active");
    menu.classList.remove("is-active");
  }
});
