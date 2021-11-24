def market_value_added(market_value, book_value):
  mvalue_added = market_value- book_value
  return mvalue_added

print(market_value_added(1000,100))

def market_to_book_ratio(market_value, book_value):
  m2b_ratio = (market_value / book_value)*1000
  m2b_ratio_rounded = round(m2b_ratio, 1)
  return m2b_ratio_rounded

print(market_to_book_ratio(222.5,1454))