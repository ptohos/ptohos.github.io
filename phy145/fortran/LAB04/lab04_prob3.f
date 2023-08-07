c========================
      program sorting
c========================
      INTEGER I, N, NMAX, NREAD
      INTEGER A(20),X, IOSTAT
      REAL    SUM, SUMSQ, PROD, AVE, STD
c
c Dinoume arxikes times sto pinaka
c==================================
      NMAX = 20         ! Megethos pinaka
      DO I = 1, NMAX
         A(I) = 0
      ENDDO
c
      open(unit=99,file='lab04_prob3.dat',status='old')

      DO 40 I =1, NMAX
 25      READ(99,*,end=35,err=30)A(I)
         goto 40                     ! No errors on read
c
 30      print *,'Error during read' ! Error during read skip the record kai
         print *,'Skipping record'   ! diabase allo stoixeio
         goto 25
c
 35      print *,'End of file before NMAX' ! End of file. Get out of the loop
         goto 10
 40   continue
 10   close(99)                      ! Close the file
c
      NRead = I - 1                  ! Tosa diavastikan
      print *,' Diavastikan ',NRead,' records'
      SUM   = 0.0
      SUMSQ = 0.0
      STD   = 0.0
      PROD  = 1.0
      DO I = 1, NRead
         SUM   = SUM + A(I)            ! Athroisma
         SUMSQ = SUMSQ + A(I)**2       ! Athroisma tetragwnwn
         PROD  = PROD*(1-A(I))         ! Ginomeno
      ENDDO
      AVE = SUM/N                      ! Mesos oros
      PRINT *,' To athroisma tetragwnwn twn stoixeiwn tou pinaka einai',
     &         SUMSQ
      PRINT *,' To ginomeno (1-A1)(1-A2)(1-A3)...(1-AN) einai',
     &         PROD
      PRINT *,' H mesi timi twn stoixeivn tou pinaka einai:', AVE
c
      DO I = 1, NRead
         STD = STD + (A(I)-AVE)**2
      ENDDO
      STD = SQRT(STD/N) 
      PRINT *,' H statheri apoklisi einai:', STD
      END
