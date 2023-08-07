      Program Draws
      Implicit None
C---------------------------------------------------------------------
      Integer M, Balls(100), Trials
      Integer Success /0/, SumA, Count /500000/
      Logical ok
      Call GetInput (M, ok)
      If (.not. ok) then
         Print*, "Invalid Entry"
      Else
         Do Trials = 1, Count
            Call Draw(M, Balls)
            If (SumA(M,Balls) .GT. 500) then
               Success = Success + 1
            End If
         End Do
         Print*, "Probability = ", Success / Float(Count)
      End If
      END

C----------------------------------------------------------------------
      Subroutine GetInput (M, ok)
      Implicit None
      Integer M
      Logical ok
      print*, "Enter number of balls to draw..."
      read*, M
      ok = (M .GT. 0) .and. (M .LT. 100)
      Return
      End

C----------------------------------------------------------------------
      Integer Function SumA(M, Balls)
      Implicit None
      Integer I, M, Balls(M), total
      total = 0
      Do I = 1, M
         total = total + Balls(I)
      End Do
      SumA = Total
      Return
      END

C----------------------------------------------------------------------
      Subroutine Draw(M, Balls)
      Implicit None
      Integer M, Balls(M), E, N
      Logical Search
      Real x
      N = 0
      Do While (N .LT. M)
         x = Rand()
         E = 1 + 100*x
         If (.NOT. Search(M, Balls, E)) then
            N = N + 1
            Balls(N) = E
         End If
      End Do
      Return
      END

C----------------------------------------------------------------------
      Logical Function Search(M, Balls, E)
      Implicit None
      Integer I, E, M, Balls(M)
      Search = .FALSE.
      Do I =1, M
         if (E .EQ. Balls(I)) then
            Search = .TRUE.
            Return
         End If
      End Do
      Return
      END
