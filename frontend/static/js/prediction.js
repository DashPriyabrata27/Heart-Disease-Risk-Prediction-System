/* ==========================================================
   prediction.js

   Project:
   --------
   Heart Disease Prediction

   Description:
   ------------
   Handles prediction-related user interface interactions.

   Responsibilities:
   -----------------
   ✓ Prevent multiple form submissions
   ✓ Display loading state
   ✓ Animate prediction result
   ✓ Animate confidence progress bar
========================================================== */

"use strict";


/* ==========================================================
   DOM Ready
========================================================== */

document.addEventListener(

    "DOMContentLoaded",

    () => {

        initializePredictionModule();

    }

);


/* ==========================================================
   Initialize Prediction Module
========================================================== */

function initializePredictionModule(){

    initializePredictionForm();

    initializeResultAnimation();

    initializeProgressBar();

}


/* ==========================================================
   Prediction Form
========================================================== */

function initializePredictionForm(){

    const predictionForm = document.querySelector(

        "form"

    );

    if(!predictionForm){

        return;

    }

    predictionForm.addEventListener(

        "submit",

        handlePrediction

    );

}


/* ==========================================================
   Handle Prediction
========================================================== */

function handlePrediction(event){

    const submitButton = document.querySelector(

        "button[type='submit']"

    );

    if(!submitButton){

        return;

    }

    submitButton.disabled = true;

    submitButton.classList.add(

        "loading"

    );

    submitButton.dataset.originalText =

        submitButton.innerHTML;

    submitButton.innerHTML =

        `
            <img
                src="/static/images/icons/loading.svg"
                alt="Loading"
                class="button-icon"
            >

            Predicting...
        `;

}
/* ==========================================================
   Result Card Animation
========================================================== */

function initializeResultAnimation(){

    const resultCard = document.querySelector(

        ".result-card"

    );

    if(!resultCard){

        return;

    }

    if(

        window.matchMedia(

            "(prefers-reduced-motion: reduce)"

        ).matches

    ){

        return;

    }

    resultCard.animate(

        [

            {

                opacity:0,

                transform:"translateY(30px)"

            },

            {

                opacity:1,

                transform:"translateY(0)"

            }

        ],

        {

            duration:700,

            easing:"ease-out",

            fill:"forwards"

        }

    );

}


/* ==========================================================
   Loading Button Animation
========================================================== */

function animateLoadingButton(){

    const submitButton = document.querySelector(

        "button[type='submit']"

    );

    if(!submitButton){

        return;

    }

    submitButton.classList.add(

        "loading"

    );

}
/* ==========================================================
   Progress Bar Animation
========================================================== */

function initializeProgressBar(){

    const progressBar = document.querySelector(

        ".progress-bar"

    );

    if(!progressBar){

        return;

    }

    const progress = Number(

        progressBar.dataset.progress

    );

    if(Number.isNaN(progress)){

        return;

    }

    progressBar.style.width = "0%";

    requestAnimationFrame(

        () => {

            setTimeout(

                () => {

                    progressBar.style.width =

                        `${progress}%`;

                },

                200

            );

        }

    );

}


/* ==========================================================
   Restore Submit Button
========================================================== */

function restoreSubmitButton(){

    const submitButton = document.querySelector(

        "button[type='submit']"

    );

    if(

        !submitButton ||

        !submitButton.dataset.originalText

    ){

        return;

    }

    submitButton.disabled = false;

    submitButton.classList.remove(

        "loading"

    );

    submitButton.innerHTML =

        submitButton.dataset.originalText;

}


/* ==========================================================
   Get Submit Button
========================================================== */

function getSubmitButton(){

    return document.querySelector(

        "button[type='submit']"

    );

}