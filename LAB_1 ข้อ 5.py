def auction(bid):

  if( len(bid) <= 1 ) :

    print("not enough bidder")

  else :

    mx = max ( bid[0] , bid[1] )

    secondmx = min ( bid[0] , bid[1] )
    
    n = len(bid)
    
    for i in range( 2 , n ):
    
      if bid[i] > mx :
    
        secondmx = mx
    
        mx = bid[i]
    
      elif bid[i] > secondmx :
    
        secondmx = bid[i]
    
    if(mx == secondmx) :
    
      print("error : have more than one highest bid")
    
    else:
    
      print("winner bid is",mx,"need to pay",secondmx)

bid = [int(e) for e in input("Enter All Bid : ").split()]

auction(bid)

