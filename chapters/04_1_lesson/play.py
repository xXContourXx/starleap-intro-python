import turtle
Steve = turtle.Turtle()
Steve.shape('turtle')
print (Steve)


Steve.color('purple', 'green')

Steve.write('Hello', font=('Comic Sans', 100, 'normal'), align='center' )

for i in range(4):
    print('Hello!')
turtle.mainloop()