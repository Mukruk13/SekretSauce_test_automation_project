from selenium.webdriver.common.by import By

class LoginPageLocators:
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.XPATH, "//h3[@data-test='error']")

class ProductPageLocators:

    CART = (By.CLASS_NAME, "shopping_cart_link")

    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_BIKE_LIGHT = (By.ID, "add-to-cart-sauce-labs-bike-light")
    ADD_BOLT_TSHIRT = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ADD_FLEECE_JACKET = (By.ID, "add-to-cart-sauce-labs-fleece-jacket")
    ADD_ONESIE = (By.ID, "add-to-cart-sauce-labs-onesie")
    ADD_RED_TSHIRT = (By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")

    REMOVE_BACKPACK = (By.ID, "remove-sauce-labs-backpack")
    REMOVE_BIKE_LIGHT = (By.ID, "remove-sauce-labs-bike-light")
    REMOVE_BOLT_TSHIRT = (By.ID, "remove-sauce-labs-bolt-t-shirt")
    REMOVE_FLEECE_JACKET = (By.ID, "remove-sauce-labs-fleece-jacket")
    REMOVE_ONESIE = (By.ID, "remove-sauce-labs-onesie")
    REMOVE_RED_TSHIRT = (By.ID, "remove-test.allthethings()-t-shirt-(red)")


    ADD_PRODUCT_LOCATORS = {
        ADD_BACKPACK: "Sauce Labs Backpack",
        ADD_BIKE_LIGHT: "Sauce Labs Bike Light",
        ADD_BOLT_TSHIRT: "Sauce Labs Bolt T-Shirt",
        ADD_FLEECE_JACKET: "Sauce Labs Fleece Jacket",
        ADD_ONESIE: "Sauce Labs Onesie",
        ADD_RED_TSHIRT: "Test.allTheThings() T-Shirt (Red)"
    }

    REMOVE_PRODUCT_LOCATORS = {
        "Sauce Labs Backpack": REMOVE_BACKPACK,
        "Sauce Labs Bike Light": REMOVE_BIKE_LIGHT,
        "Sauce Labs Bolt T-Shirt": REMOVE_BOLT_TSHIRT,
        "Sauce Labs Fleece Jacket": REMOVE_FLEECE_JACKET,
        "Sauce Labs Onesie": REMOVE_ONESIE,
        "Test.allTheThings() T-Shirt (Red)": REMOVE_RED_TSHIRT
    }

class YourCartLocators:

    INVENTORY_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")

    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")

    REMOVE_BACKPACK = (By.ID, "remove-sauce-labs-backpack")
    REMOVE_BIKE_LIGHT = (By.ID, "remove-sauce-labs-bike-light")
    REMOVE_BOLT_TSHIRT = (By.ID, "remove-sauce-labs-bolt-t-shirt")
    REMOVE_FLEECE_JACKET = (By.ID, "remove-sauce-labs-fleece-jacket")
    REMOVE_ONESIE = (By.ID, "remove-sauce-labs-onesie")
    REMOVE_RED_TSHIRT = (By.ID, "remove-test.allthethings()-t-shirt-(red)")

    REMOVE_PRODUCT_LOCATORS = {
        "Sauce Labs Backpack": REMOVE_BACKPACK,
        "Sauce Labs Bike Light": REMOVE_BIKE_LIGHT,
        "Sauce Labs Bolt T-Shirt": REMOVE_BOLT_TSHIRT,
        "Sauce Labs Fleece Jacket": REMOVE_FLEECE_JACKET,
        "Sauce Labs Onesie": REMOVE_ONESIE,
        "Test.allTheThings() T-Shirt (Red)": REMOVE_RED_TSHIRT
    }

class CheckoutYourInformationLocators:
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

class CheckoutOverviewLocators:
    FINISH_BUTTON = (By.ID, "finish")

class CheckoutCompleteLocators:
    BACK_TO_PRODUCTS_BUTTON = (By.ID, "back-to-products")
