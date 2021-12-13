def market_value_added(market_value, book_value):
  mvalue_added = market_value- book_value
  return mvalue_added

print(market_value_added(1000,100))

def market_to_book_ratio(market_value, book_value):
  m2b_ratio = (market_value / book_value)*1000
  m2b_ratio_rounded = round(m2b_ratio, 1)
  return m2b_ratio_rounded

print(market_to_book_ratio(222.5,1454))

def total_capitalization(longterm_debt, shareholders_equity):
  return longterm_debt + shareholders_equity

print(total_capitalization(100,100))

def fv_for_savings(pv,interest_rate,terms):
  return pv*((1+interest_rate)^terms)

def bond_yield(ann_cuopon_payment,bond_price):
  return ann_cuopon_payment/bond_price