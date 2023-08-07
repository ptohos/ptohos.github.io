c==========================================================
      program ellipsis_area
c==========================================================
c Eyresi tis timis tou pi me ti methodo Monte Carlo
c
c Opws kai stin periptwsi tis askisis 5 toy ergastiriou 9
c orizoume ena parallilogrammo me mikos pleuras a=3 kai b=2,
c to opoio perikleiei to ena tetartimorio tis elleipsis.
c To embado tou parallilogrammou einai a*b. 
c Epilegoume tyxaia simeia x sto diastima [0,3] kai y sto 
c diastima [0,2] ta opoia zitoume na ikanopoioun tin eksiswsi
c tis elleipsis x**2/a**2 + y**2/b**2 <= 1. 
c To embado tis elleipsis tha einai tote: E = a*b*Nellip./Ntot
c===========================================================
      implicit none
      integer  j, k
      integer  N_pass, N_tot
      integer  iseed
      data iseed/123456/
      real*8   Area_the, Area_MC
      real*8   xrand, yrand
      real*8   el, R_el
      real*8   a, b, pi
      parameter(a=3d0)
      parameter(b=2d0)
      parameter(pi=dacos(-1d0))
      parameter(R_el=1.0)
      real*8   integral

      
      xrand = rand(iseed)     ! Ksekinima tis akolouthias twn tuxaiwn arithmwn
      do j =1, 6
         N_tot = 10**j        ! Arithmos prospatheiwn
         N_pass = 0           ! Midenismos twn simeiwn me x**2/a**2+y**2/b**2<1
         if (j.eq.1) write(6,29)
         do k = 1, N_tot
            xrand = a*rand()    ! Tyxaio simeio sto diastima [0,a]
            yrand = b*rand()    ! Tyxaio simeio sto diastima [0,b]
            el = xrand**2/a**2 + yrand**2/b**2
            if (el.le.R_el**2) N_pass = N_pass + 1
         enddo
         integral = dble(N_pass)/dble(N_tot)
         Area_MC = 4D0* integral * a * b
         Area_the = pi * a * b
         write(6,30) N_tot, Area_MC, Area_the, abs(Area_MC - Area_the)
      enddo
 29   format(5x,'Ntries',3x,'Area ala MC',3x,'Area Theory',5x,'Diafora')
 30   format(3x,i7,5x,f9.6,5x,f9.6,5x,f9.7)
      end
