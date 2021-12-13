# Sleeping Dragon Hobby Shop - Testing 

## Contents 
- [Automated Testing](#automated-testing)
    - [HTML](#html)
    - [Custom CSS Styling](#custom-css-styling)
    - [JavaScript Code Testing](#javascript-code-testing)
    - [Python Code Testing](#python-code-testing)
    - [Automated Performance And Quality Testing](#automated-performance-and-quality-testing)
- [User Stories Testing](#user-stories-testing)
- [Manual Testing](#manual-testing)
    - [Features](#features)
        - [Home](#home)
        - [Base Template](#base-template)
        - [User Authentication](#user-authentication)
        - [Contact](#contact)
        - [Products](#products)
        - [Basket](#basket)
        - [Checkout](#checkout)
        - [User Profile](#user-profile)
    - [Form Validation](#form-validation)
    - [Responsive Design Testing](#responsive-design-testing)
    - [Browser Compatibility Testing](#browser-compatibility-testing)
    - [Stripe Webhook Handler Testing](#stripe-webhook-handler-testing)
    - [Restricted Features Security Testing](#restricted-features-security-testing)
- [Bugs Fixed During Testing](#bugs-fixed-during-testing)
- [Bugs Remaining](#bugs-remaining)

## Automated Testing 

### HTML 
All **HTML** code was validated using the [W3C Markup Validation Service](https://validator.w3.org/) 
regularly during the development process. **The HTML Source Code** was regularly viewed for each page 
using **Chrome Developer Tools** (right click, *Inspect*) and passed through the 
[W3C Markup Validation Service](https://validator.w3.org/).  
Various minor errors were encountered and corrected during the final **HTML** validation check. 
All HTML code now passes validation with no errors or warnings. See [HTML Validation Reports](media/testing/validation/html).

### CSS
Custom CSS from [base.css](static/css/base.css), [profile.css](profiles/static/profiles/css/profile.css) and [checkout.css](checkout/static/checkout/css/checkout.css) was validated using the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/).  
No errors were generated.