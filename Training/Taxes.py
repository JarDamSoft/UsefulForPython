def taxes(state, gross):
    state_tax = 0
    if state == "New York".lower() or state == "Alabama".lower() or state == "Georgia".lower():
        state_tax = gross * 0.1
    elif state == "Nevada".lower() or state == "California".lower():
        state_tax = gross * 0.08
    else:
        state_tax = gross * 0.04
    federal = gross * 0.1
    netto = gross - (state_tax + federal)
    # print("Your netto income after all the taxes, will be: {}".format(netto))
    print("Your netto income after all the taxes, will be:" + str(netto))
    print(f"Your netto income after all the taxes, will be: ${netto:,.2f}")
    return netto


# tax_value = taxes("bedzin", 25000)
# print("Your netto income will be: {}" .format(tax_value))


taxes("alabama", 100000)