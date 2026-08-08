/* ==========================================================
   form_validation.js

   Project:
   --------
   Heart Disease Prediction

   Description:
   ------------
   Client-side validation for the prediction form.

   Responsibilities:
   -----------------
   ✓ Validate user inputs
   ✓ Display validation errors
   ✓ Prevent invalid form submission
   ✓ Improve user experience
========================================================== */

"use strict";


/* ==========================================================
   DOM Ready
========================================================== */

document.addEventListener(

    "DOMContentLoaded",

    () => {

        initializeValidation();

    }

);


/* ==========================================================
   Initialize Validation
========================================================== */

function initializeValidation(){

    const predictionForm = document.querySelector(

        "form"

    );

    if(!predictionForm){

        return;

    }

    predictionForm.addEventListener(

        "submit",

        validateForm

    );

    initializeRealtimeValidation();

}


/* ==========================================================
   Real-Time Validation
========================================================== */

function initializeRealtimeValidation(){

    attachNumberValidation(

        "age",

        validateAge

    );

    attachNumberValidation(

        "height",

        validateHeight

    );

    attachNumberValidation(

        "weight",

        validateWeight

    );

    attachNumberValidation(

        "ap_hi",

        validateSystolicBP

    );

    attachNumberValidation(

        "ap_lo",

        validateDiastolicBP

    );

    attachSelectValidation(

        "gender"

    );

    attachSelectValidation(

        "cholesterol"

    );

    attachSelectValidation(

        "gluc"

    );

    attachSelectValidation(

        "smoke"

    );

    attachSelectValidation(

        "alco"

    );

    attachSelectValidation(

        "active"

    );

}


/* ==========================================================
   Number Input Validation
========================================================== */

function attachNumberValidation(

    elementId,

    validator

){

    const input = document.getElementById(

        elementId

    );

    if(!input){

        return;

    }

    input.addEventListener(

        "input",

        () => validator(input)

    );

}


/* ==========================================================
   Select Validation
========================================================== */

function attachSelectValidation(

    elementId

){

    const select = document.getElementById(

        elementId

    );

    if(!select){

        return;

    }

    select.addEventListener(

        "change",

        () => {

            clearError(select);

        }

    );

}


/* ==========================================================
   Show Validation Error
========================================================== */

function showError(

    input,

    message

){

    clearError(input);

    input.classList.add(

        "invalid"

    );

    const error = document.createElement(

        "small"

    );

    error.className = "validation-error";

    error.textContent = message;

    input.parentElement.appendChild(

        error

    );

}


/* ==========================================================
   Clear Validation Error
========================================================== */

function clearError(

    input

){

    input.classList.remove(

        "invalid"

    );

    const error = input.parentElement.querySelector(

        ".validation-error"

    );

    if(error){

        error.remove();

    }

}
/* ==========================================================
   Generic Range Validator
========================================================== */

function validateRange(

    input,

    minimum,

    maximum,

    requiredMessage,

    rangeMessage

){

    clearError(input);

    const value = Number(input.value);

    if(input.value.trim() === ""){

        showError(

            input,

            requiredMessage

        );

        return false;

    }

    if(value < minimum || value > maximum){

        showError(

            input,

            rangeMessage

        );

        return false;

    }

    return true;

}


/* ==========================================================
   Age Validation
========================================================== */

function validateAge(input){

    return validateRange(

        input,

        1,

        120,

        "Age is required.",

        "Age must be between 1 and 120 years."

    );

}


/* ==========================================================
   Height Validation
========================================================== */

function validateHeight(input){

    return validateRange(

        input,

        50,

        250,

        "Height is required.",

        "Height must be between 50 cm and 250 cm."

    );

}


/* ==========================================================
   Weight Validation
========================================================== */

function validateWeight(input){

    return validateRange(

        input,

        10,

        300,

        "Weight is required.",

        "Weight must be between 10 kg and 300 kg."

    );

}


/* ==========================================================
   Systolic Blood Pressure
========================================================== */

function validateSystolicBP(input){

    return validateRange(

        input,

        50,

        250,

        "Systolic blood pressure is required.",

        "Systolic blood pressure must be between 50 and 250 mmHg."

    );

}


/* ==========================================================
   Diastolic Blood Pressure
========================================================== */

function validateDiastolicBP(input){

    return validateRange(

        input,

        30,

        200,

        "Diastolic blood pressure is required.",

        "Diastolic blood pressure must be between 30 and 200 mmHg."

    );

}


/* ==========================================================
   Blood Pressure Relationship
========================================================== */

function validateBloodPressure(){

    const systolic = document.getElementById(

        "ap_hi"

    );

    const diastolic = document.getElementById(

        "ap_lo"

    );

    if(!systolic || !diastolic){

        return true;

    }

    const systolicValue = Number(

        systolic.value

    );

    const diastolicValue = Number(

        diastolic.value

    );

    if(

        systolic.value.trim() === "" ||

        diastolic.value.trim() === ""

    ){

        return false;

    }

    if(systolicValue <= diastolicValue){

        showError(

            systolic,

            "Systolic pressure must be greater than diastolic pressure."

        );

        showError(

            diastolic,

            "Diastolic pressure must be lower than systolic pressure."

        );

        return false;

    }

    clearError(systolic);

    clearError(diastolic);

    return true;

}


/* ==========================================================
   Select Field Validation
========================================================== */

function validateSelectField(

    elementId,

    message

){

    const select = document.getElementById(

        elementId

    );

    if(!select){

        return true;

    }

    clearError(select);

    if(select.value === ""){

        showError(

            select,

            message

        );

        return false;

    }

    return true;

}
/* ==========================================================
   Form Validation
========================================================== */

function validateForm(event){

    let isValid = true;

    const age = document.getElementById("age");
    const height = document.getElementById("height");
    const weight = document.getElementById("weight");
    const systolic = document.getElementById("ap_hi");
    const diastolic = document.getElementById("ap_lo");

    if(!validateAge(age)){

        isValid = false;

    }

    if(!validateHeight(height)){

        isValid = false;

    }

    if(!validateWeight(weight)){

        isValid = false;

    }

    if(!validateSystolicBP(systolic)){

        isValid = false;

    }

    if(!validateDiastolicBP(diastolic)){

        isValid = false;

    }

    if(!validateBloodPressure()){

        isValid = false;

    }

    const selectFields = [

        {
            id:"gender",
            message:"Please select gender."
        },

        {
            id:"cholesterol",
            message:"Please select cholesterol level."
        },

        {
            id:"gluc",
            message:"Please select glucose level."
        },

        {
            id:"smoke",
            message:"Please select smoking status."
        },

        {
            id:"alco",
            message:"Please select alcohol consumption."
        },

        {
            id:"active",
            message:"Please select physical activity."
        }

    ];

    selectFields.forEach(

        (field) => {

            if(

                !validateSelectField(

                    field.id,

                    field.message

                )

            ){

                isValid = false;

            }

        }

    );

    if(!isValid){

        event.preventDefault();

        focusFirstInvalidField();

        return false;

    }

    return true;

}


/* ==========================================================
   Focus First Invalid Field
========================================================== */

function focusFirstInvalidField(){

    const firstInvalidField = document.querySelector(

        ".invalid"

    );

    if(firstInvalidField){

        firstInvalidField.focus();

    }

}