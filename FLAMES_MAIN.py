def remove_common_chars(name_1,name_2):
    for char in name_1[:]:
        if char in name_2:
            name_1.remove(char)
            name_2.remove(char)
    return name_1,name_2
    
def name_space_remover(name_1,name_2):
        n1=""
        n2=""
        for char_n1 in name_1[:]:
            if char_n1 ==" ":
                pass
            else:
                n1+=char_n1
        for char_n2 in name_2[:]:       
            if char_n2 ==" ":
                pass
            else:
                n2+=char_n2
        return n1,n2   
        
def special_keys_finder(name_1,name_2):
    n1=name_1.isalpha()
    n2=name_2.isalpha()
    return n1,n2      
    
def calculate_flames(name_1, name_2):
    total_chars = int(len(name_1) + len(name_2))
    if total_chars in [3,5,14,16,18,21,23]:  
      return "Friends"  
    elif total_chars in [10,19]:  
      return "in Love"  
    elif total_chars in [8,12,13,17]:  
      return "Affectionate"  
    elif total_chars in [6,11,15]:  
      return "Married"  
    elif total_chars in [2,4,7,9,20,22,24,25]:  
      return "Enemies"  
    elif total_chars in [1]:
      return "Siblings"
    else:
        return "\nSorry,Try again"    

def main():
    while True:
        name_1 = input('\nEnter Your Name:').lower()
        if len(name_1) <4:
            print("\nPlease Enter Your Name Correctly")
            continue
            
        while True:
            name_2 = input('Enter Your Admirer Name:').lower()
            if len(name_2) <4:
                print("\nPlease Enter Your Admirer Name Correctly\n")
                continue 
            break 
                  
        name_1,name_2 = name_space_remover(name_1,name_2)
        skf1,skf2=special_keys_finder(name_1,name_2)
    
        if skf1 and skf2 is True:
            pass
        else:
            print("\nDon't use numbers and special characters like @#₹_& etc...")
            break
        
        name_1,name_2 = remove_common_chars(list(name_1), list(name_2))
        result = calculate_flames(name_1,name_2)
        
        if result!="Sorry,Try again":
            print('\nYou both are',result,"\n")
        else:
            print(result)
            
        user_in=input("Do you want to continue?\nYes/No:").lower()
        
        if user_in =="yes":
            pass
        elif user_in =="no":
            print("\nThank you for using!")
            break
        else:
            print("\nSorry,I cant understand")
            print("\nThank you for using!")
            break
            
Head='FLAMES'
print(Head.center(37,'*'))
main()
    