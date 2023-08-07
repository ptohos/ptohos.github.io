c==========================================================
      program montecarlo_pi
c==========================================================
c Eyresi tis timis tou pi me ti methodo Monte Carlo
c
c Gia na to epitixoume orizoume ena imikuklio
c aktinas R=1 to opoio einai eggegrammeno 
c se ena tetragwno pleuras 1. 
c To embado tou imikukliou einai (pi*R**2)/4 = pi/4
c To embado tou antistoixou tetragwnou einai a**2=R**2=1
c Sumfvna me ti methodo epilogis Monte Carlo tha prepei 
c ksekinontas apo tyxaia simeia (x,y) sto diastima [0,1]
c na metrisoume to pososto twn simeiwn pou ikanopoioun 
c ti sxesi x**2+y**2 <= 1. Tote to pososto ayto tha einai 
c iso me to logo twn embadwn tou imikukliou kai tetragwnou
c  N(R**2<=1)/Ntot = E_imikikliou/E_tetragwnou = Pi/4
c===========================================================
      implicit none
      integer  j, k
      integer  N_pass, N_tot
      integer  iseed
      data iseed/123456/
      real*8   xrand, yrand
      real*8   R, R_circ
      parameter(R_circ=1.0)
      real*8   integral, pi

      xrand = rand(iseed)     ! Ksekinima tis akolouthias twn tuxaiwn arithmwn
      do j =1, 8
         N_tot = 10**j        ! Arithmos prospatheiwn
         N_pass = 0           ! Midenismos twn simeiwn me R**2<R_circ**2
         if (j.eq.1) write(6,29)
         do k = 1, N_tot
            xrand = rand()    ! Tyxaio simeio sto diastima [0,1]
            yrand = rand()    ! Tyxaio simeio sto diastima [0,1]
            R = xrand**2 + yrand**2
            if (R.le.R_circ**2) N_pass = N_pass + 1
         enddo
         integral = dble(N_pass)/dble(N_tot)
         pi       = 4*integral
         write(6,30) N_tot, pi
      enddo
 29   format(5x,'Ntries',3x,'Pi value')
 30   format(2x,i9,2x,f9.7)
      end
