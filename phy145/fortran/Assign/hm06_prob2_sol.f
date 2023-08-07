      program moment_of_inertia
c===================================
c To programma upologizei ti ropi 
c adraneias enos diskou D aktinas 
c R=1 kai kentro (0,0) ws pros ena
c tyxaio simeio me suntetagmenes (xo,yo) 
c xrisimopoiwntas ti methodo Monte
c Carlo
c=====================================
      implicit none
      integer Ntrials, Npnts
      integer iseed, j
      data iseed/123456/
      real*8 x0, y0, x, y, dx, dy
      real*8 sum, MomOfInertia
      real*8 radius
c
      real rand

c...Arxi tis akoloythias twn tyxaiwn arithmwn
      call srand(iseed)
c
      print *,'Dwste tin aktina tou diskou, R'
      read *, radius
      print *,'Dwste tis syntetagmenes tou tyxaio simeiou (xo,yo)'
      read *, x0,y0
      print *,'Dwste ton arithmo twn simeiwn'
      read *,Ntrials
c
      sum = 0.0D0
      Npnts = 0
c
      do while (Npnts .le. Ntrials)
         x = 2.0d0*rand() - 1.0d0
         y = 2.0d0*rand() - 1.0d0
         if ((x**2 + y**2) .le. radius) then  ! To simeio anikei sto disko
            Npnts = Npnts + 1
            dx = x - x0
            dy = y - y0
            sum = sum + (dx*dx + dy*dy) 
         endif
      enddo
c
      MomOfInertia = sum/Npnts
      write(6,10)x0,y0,MomOfInertia
 10   format(1x,'H ropi adraneias tou diskou ws pros to simeio (',f6.3,
     &      ',',f6.3,') einai:',1x,f8.6)
      end
