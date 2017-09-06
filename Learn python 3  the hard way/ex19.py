def cheese_and_crackers(cheese_count,boxes_of_cracker):
    print(f"Cheese count: {cheese_count}")
    print(f"No of boxes of cracker avalible: {boxes_of_cracker}")
    while(cheese_count>0):
        cheese_count = cheese_count-10
        cheese_and_crackers(cheese_count,boxes_of_cracker)



cheese_and_crackers(20,30)
#a = 10
#b = 30
#cheese_and_crackers(a,b)

#cheese_and_crackers(10+15,20+30)
