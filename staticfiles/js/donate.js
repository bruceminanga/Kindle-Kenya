 // Wait for the document to be fully loaded
  document.addEventListener("DOMContentLoaded", function () {
    // Initialize variables
    let selectedAmount = null;
    let selectedPaymentMethod = null;
    const currencySymbols = {
      USD: "$",
      EUR: "€",
      GBP: "£",
      KES: "KSh",
    };

    // Get DOM elements
    const amountButtons = document.querySelectorAll(".amount-preset");
    const customAmountBtn = document.getElementById("custom-amount");
    const customAmountInput = document.getElementById("custom-amount-input");
    const paymentMethodButtons = document.querySelectorAll(
      ".payment-method-btn"
    );
    const phoneField = document.getElementById("phone-field");
    const currencySelect = document.getElementById("currency");
    const currencySymbol = document.querySelector(".currency-symbol");
    const form = document.getElementById("donation-form");

    // Handle amount preset selection
    function handleAmountSelection(e) {
      // Remove active class from all buttons
      amountButtons.forEach((btn) => btn.classList.remove("active"));
      customAmountBtn.classList.remove("active");
      customAmountInput.style.display = "none";

      // Add active class to clicked button
      e.target.classList.add("active");
      selectedAmount = e.target.dataset.amount;
    }

    // Handle custom amount button
    function handleCustomAmount() {
      amountButtons.forEach((btn) => btn.classList.remove("active"));
      customAmountBtn.classList.add("active");
      customAmountInput.style.display = "block";
      selectedAmount = null;
    }

    // Handle payment method selection
    function handlePaymentMethod(e) {
      // Remove active class from all payment buttons
      paymentMethodButtons.forEach((btn) => btn.classList.remove("active"));

      // Add active class to clicked button
      e.target.classList.add("active");
      selectedPaymentMethod = e.target.dataset.method;

      // Show/hide payment specific sections
      document.querySelectorAll(".payment-section").forEach((section) => {
        section.style.display = "none";
      });

      // Show selected payment method section
      const selectedSection = document.getElementById(
        `${selectedPaymentMethod}-payment`
      );
      if (selectedSection) {
        selectedSection.style.display = "block";
      }

      // Show/hide phone field for M-PESA
      phoneField.style.display =
        selectedPaymentMethod === "mpesa" ? "block" : "none";
    }

    // Handle currency change
    function handleCurrencyChange(e) {
      const symbol = currencySymbols[e.target.value];
      currencySymbol.textContent = symbol;

      // Show/hide M-PESA option based on currency
      const mpesaButton = document.querySelector('[data-method="mpesa"]');
      if (mpesaButton) {
        mpesaButton.closest(".col-md-4").style.display =
          e.target.value === "KES" ? "block" : "none";
      }
    }

    // Form validation and submission
    function handleFormSubmit(e) {
      e.preventDefault();

      if (!form.checkValidity()) {
        e.stopPropagation();
        form.classList.add("was-validated");
        return;
      }

      if (!selectedPaymentMethod) {
        alert("Please select a payment method");
        return;
      }

      if (!selectedAmount && !document.getElementById("amount").value) {
        alert("Please select or enter an amount");
        return;
      }

      // Show processing overlay
      document.querySelector(".processing-overlay").style.display = "flex";

      // Collect form data
      const formData = {
        amount: selectedAmount || document.getElementById("amount").value,
        currency: currencySelect.value,
        paymentMethod: selectedPaymentMethod,
        firstName: document.getElementById("firstName").value,
        lastName: document.getElementById("lastName").value,
        email: document.getElementById("email").value,
        message: document.getElementById("message").value,
        phone: document.getElementById("phone").value,
      };

      // Here you would typically make an API call to your backend
      console.log("Form submission data:", formData);

      // Simulate API call (remove this in production)
      setTimeout(() => {
        document.querySelector(".processing-overlay").style.display = "none";
        alert("Donation form submitted successfully!");
        form.reset();
        resetFormState();
      }, 2000);
    }

    // Reset form state
    function resetFormState() {
      selectedAmount = null;
      selectedPaymentMethod = null;
      amountButtons.forEach((btn) => btn.classList.remove("active"));
      paymentMethodButtons.forEach((btn) => btn.classList.remove("active"));
      customAmountBtn.classList.remove("active");
      customAmountInput.style.display = "none";
      document.querySelectorAll(".payment-section").forEach((section) => {
        section.style.display = "none";
      });
      phoneField.style.display = "none";
      form.classList.remove("was-validated");
    }

    // Add event listeners
    amountButtons.forEach((button) => {
      button.addEventListener("click", handleAmountSelection);
    });

    customAmountBtn.addEventListener("click", handleCustomAmount);

    paymentMethodButtons.forEach((button) => {
      button.addEventListener("click", handlePaymentMethod);
    });

    currencySelect.addEventListener("change", handleCurrencyChange);

    form.addEventListener("submit", handleFormSubmit);
  });
