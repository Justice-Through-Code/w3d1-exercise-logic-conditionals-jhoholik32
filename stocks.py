
def stock_purchases():
    amazon = 3000
    apple = 100
    fb = 250
    google = 1400
    msft = 200

    # Given the prices above and a client's investment budget, how much stock can they buy?
    # 1.1 TODO: Ask the client's name (use the string: "What is your name? ") and save it into a variable
    name=input("What is your name? ")
    # 1.2 TODO: Ask the client how many dollars they would like to invest (use the string: "How much would you like to invest? $")
    # and save it into a variable
    # NOTE: When you use the `input` function to get user input, what do numbers get saved as?
    invest_amount = int(input("How much would you like to invest? $"))
    print(invest_amount)
    # 1.3 TODO: Uncomment the line below to ask the client which stock they're interested in.
    # NOTE: Take a look at how this input string prints out
    stock_name = input("\nWhich stock are you interested in? Enter the full name:\nAmazon\nApple\nFacebook\nGoogle\nMicrosoft\nStock Name: ")
    print(apple)
    # Use `if/elif/else` conditional logic to determine how much stock the client can buy,
    # and save it in a variable
    shares = invest_amount /
    if stock_name == "amazon":
        shares = invest_amount / amazon
        print(amazon)
    elif stock_name == "apple":
       shares = invest_amount / apple 
       print(apple)
    elif stock_name == "fb":
       shares = invest_amount / fb  
       print(fb)
    elif stock_name == "google":
       shares = invest_amount / google
       print(google)
    elif stock_name == "msft":
        shares = invest_amount / msft 
        print(msft)
    else:
        print("invalid stock name entered")
    print(f"{name} has ${invest_amount} to invest and can buy {shares} shares of Apple at the current price of ${apple}. ")    
    # 1.5 TODO: Once you've calculated the number of stocks that can be purchased,
    # Use an f-string to print the result for the client, ala:
    # Alex has $5000 to invest and can buy 50 shares of Apple at the current price of $100.