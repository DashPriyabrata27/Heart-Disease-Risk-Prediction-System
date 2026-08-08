/* ==========================================================
   ui.js

   Project:
   --------
   Heart Disease Prediction

   Description:
   ------------
   Handles global user interface interactions,
   animations, navigation behavior, and common
   page enhancements.
========================================================== */

"use strict";


/* ==========================================================
   DOM Ready
========================================================== */

document.addEventListener(

    "DOMContentLoaded",

    () => {

        initializeApplication();

    }

);


/* ==========================================================
   Initialize Application
========================================================== */

function initializeApplication(){

    initializeNavbar();

    initializeScrollAnimation();

    initializeScrollToTop();

    initializeActiveNavigation();

}


/* ==========================================================
   Navbar Shadow Effect
========================================================== */

function initializeNavbar(){

    const navbar = document.querySelector(

        ".navbar"

    );

    if(!navbar){

        return;

    }

    window.addEventListener(

        "scroll",

        () => {

            if(window.scrollY > 50){

                navbar.classList.add(

                    "navbar-scrolled"

                );

            }

            else{

                navbar.classList.remove(

                    "navbar-scrolled"

                );

            }

        },

        {

            passive:true

        }

    );

}
/* ==========================================================
   Fade-In Animation
========================================================== */

function initializeScrollAnimation(){

    const animatedElements = document.querySelectorAll(

        ".hero, .form-card, .result-card, .error-container"

    );

    if(animatedElements.length === 0){

        return;

    }

    const observer = new IntersectionObserver(

        (entries) => {

            entries.forEach(

                (entry) => {

                    if(entry.isIntersecting){

                        entry.target.classList.add(

                            "fade-in"

                        );

                        observer.unobserve(

                            entry.target

                        );

                    }

                }

            );

        },

        {

            threshold:0.15

        }

    );

    animatedElements.forEach(

        (element) => {

            observer.observe(

                element

            );

        }

    );

}


/* ==========================================================
   Scroll-To-Top Button
========================================================== */

function initializeScrollToTop(){

    const scrollButton = document.getElementById(

        "scrollToTop"

    );

    if(!scrollButton){

        return;

    }

    window.addEventListener(

        "scroll",

        () => {

            if(window.scrollY > 300){

                scrollButton.classList.add(

                    "show"

                );

            }

            else{

                scrollButton.classList.remove(

                    "show"

                );

            }

        },

        {

            passive:true

        }

    );

    scrollButton.addEventListener(

        "click",

        () => {

            window.scrollTo(

                {

                    top:0,

                    behavior:"smooth"

                }

            );

        }

    );

}
/* ==========================================================
   Active Navigation
========================================================== */

function initializeActiveNavigation(){

    const currentPath = normalizePath(

        window.location.pathname

    );

    const navigationLinks = document.querySelectorAll(

        ".nav-links a"

    );

    navigationLinks.forEach(

        (link) => {

            const linkPath = normalizePath(

                new URL(

                    link.href,

                    window.location.origin

                ).pathname

            );

            if(linkPath === currentPath){

                link.classList.add(

                    "active"

                );

            }

        }

    );

}


/* ==========================================================
   Normalize URL Path
========================================================== */

function normalizePath(path){

    if(path.length > 1 && path.endsWith("/")){

        return path.slice(0, -1);

    }

    return path;

}


/* ==========================================================
   Utility Function
========================================================== */

function elementExists(selector){

    return document.querySelector(selector) !== null;

}