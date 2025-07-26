
def main():
    try:
      a=int(input("hey,enter a number:"))

      print(a)
      return

    except Exception as e:
      print(e)
      return
    finally:   #finally chalta hi chalta chae try(run) main jae ya expect mian jae (error)
     print("I am inside in finally") 
   
main()




    