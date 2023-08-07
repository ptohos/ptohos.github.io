c====================================================
      program ChargeInEMField
c====================================================
c Kinisi ilektrika fortismenou swmatidiou, fortiou q,
c kai mazas,m, mesa se hlektromagnitiko pedio. 
c H dunami Lorentz einai F = q(E + uxB) opote oi 
c exiswseis tis epitaxunsis tou swmatidiou tha einai:
c a(1) = ax = q/m[Ex + (uy*Bz - uz*By)]
c a(2) = ay = q/m[Ey - (ux*Bz - uz*Bx)]
c a(3) = az = q/m[Ez + (ux*By - uy*Bx)] 
c H epilusi twn exiswsewn ginetai me tis methodous 
c Euler-Cromer kai Runge-Kutta 4ou vathmou
c
c H energeia tou swmatidiou dinetai apo tin exiswsi
c E = Ekin + Edyn = 0.5*m*|v|^2 - q(Ex*x+Ey*y+Ez*z)  
c Stin periptwsi pou E=0 i kinitiki energeia tou
c swmatidiou paramenei statheri afou i dynami tou 
c pediou einai katheti stin taxytita kai epomenws 
c den paragei ergo. Otan E#0 tote to swmatidio 
c ayksanei tin energeia tou. 
c Wstoso i methodos Euler-Cromer den diatirei tin 
c energeia parolo pou i troxia pou vlepoume einai 
c kukliki opws tha perimename otan E=0 
c
c Gia na deite ta grafimata tis troxias mporeite 
c na dwsete tis akolouthes entoles sto gnuplot: 
c
c set xyplane at 0 
c set view 60,140
c set xlabel 'x'
c set ylabel 'y'  
c set zlabel 'z'  
c splot "trajectory1.dat" u 2:3:4 w lines, "trajectory2.dat" u 2:3:4 w lines 
c====================================================
      implicit none
      integer j, lun
      real*8 r0(3), r(3)
      real*8 u0(3), u(3)
      real*8 accel(3)
      real*8 Bfield(3), Efield(3), Efld(3)
      real*8 mass, q
      real*8 time0,tmax,tchange
      real*8 time,dt
      real*8 Energy, Ene
      logical first

      q       = 1D0
      mass    = 1D0
      tmax    = 4D1
      tchange = 1D1
      time0   = 0
      time    = time0
      dt      = 4D-2
c... Oi 3 sunistwses tis arxikis taxytitas
      u0(1) = 0D0
      u0(2) = 1D0
      u0(3) = 1D-1
c... Oi 3 sunistwses tou arxikou dianusmatos thesis
      r0(1) = 1D0
      r0(2) = 0D0
      r0(3) = 0D0
c... Oi 3 sunistwses tou magnitikou pediou
      Bfield(1)  = 0D0
      Bfield(2)  = 0D0
      Bfield(3)  = 1D0
c... Oi 3 sunistwses tou ilektrikou pediou     
      Efld(1)  = 1D-1
      Efld(2)  = 1D-1
      Efld(3)  = 0D0
c... Apothikeusi arxikwn sunthikwn taxytitas kai thesis
      do j=1, 3
         u(j) = u0(j)
         r(j) = r0(j)
         Efield(j) = 0D0
      enddo

      open(unit=10,file='trajectory1.dat',status='unknown')
      open(unit=11,file='trajectory2.dat',status='unknown')

      first = .true.
      lun   = 10


      do while (time.le.tmax)

         Ene = Energy(r,u,Efield,q,mass)
         write(lun,20)time, (r(j),j=1,3), (u(j),j=1,3), Ene
         time = time + dt

         if (time .lt. tchange) then    ! E(1)=E(2)=E(3)=0
            call eulercromer(r,u,Efield,Bfield,dt,q,mass)
         else                           ! Anavoume to ilektriko pedio
            if (first) then
               Do j=1,3
                  Efield(j) = Efld(j)   ! Allagi tou pediou
                  lun   = 11            ! Allago file
                  first = .false.
               enddo
            endif
            call rk4(r,u,Efield,Bfield,dt,q,mass)
         endif

      enddo
 20   Format(1x,F5.2,6(2x,F7.4),2x,F7.4)
      close(10)
      close(11)
      end

c===============================================
      subroutine calc_accel(u,E,B,q,m,accel)
c===============================================
      implicit none
      real*8 u(3), E(3), B(3)
      real*8 q, m, accel(3)

      accel(1) = q/m * ( E(1) + ( u(2)*B(3)-u(3)*B(2) ) )
      accel(2) = q/m * ( E(2) - ( u(1)*B(3)-u(3)*B(1) ) )
      accel(3) = q/m * ( E(3) + ( u(1)*B(2)-u(2)*B(1) ) )
      return
      end

c======================================================
      subroutine eulercromer(r,u,Efield,Bfield,dt,q,m)
c======================================================
      implicit none
      integer j
      real*8 q,m,dt
      real*8 r(3), u(3)
      real*8 Efield(3), Bfield(3)
      real*8 accel(3)

      call calc_accel(u,Efield,Bfield,q,m,accel)
      
      do j = 1, 3
         u(j) = u(j) + accel(j)*dt
         r(j) = r(j) + u(j)*dt
      enddo
      return
      end


c==============================================
      subroutine rk4(r,u,Efield,Bfield,dt,q,m)
c==============================================
      implicit none
      integer j
      real*8 q,m,dt,halfdt
      real*8 r(3), u(3)
      real*8 u0(3), r0(3)
      real*8 Efield(3), Bfield(3)
      real*8 accel(3)
      real*8 k1_u(3), k2_u(3), k3_u(3), k4_u(3)
      real*8 k1_r(3), k2_r(3), k3_r(3), k4_r(3)

      halfdt = dt/2d0
      do j = 1, 3
         u0(j) = u(j)
         r0(j) = r(j)
      enddo
      
      call calc_accel(u0,Efield,Bfield,q,m,accel) ! Paragwgoi stin arxi
      do j = 1, 3
         k1_u(j) = accel(j)
         k1_r(j) = u0(j)

         u(j) = u0(j) + k1_u(j)*halfdt ! Kinisi sto meso tou diastimatos
         r(j) = r0(j) + k1_r(j)*halfdt
      enddo

      call calc_accel(u,Efield,Bfield,q,m,accel) ! Paragwgoi sto meso 
      do j = 1, 3
         k2_u(j) = accel(j)
         k2_r(j) = u(j)
         
         u(j) = u0(j) + k2_u(j)*halfdt     ! Kinisi sto meso me tis paragwgous
         r(j) = r0(j) + k2_r(j)*halfdt     ! sto meso 
      enddo

      call calc_accel(u,Efield,Bfield,q,m,accel) ! Paragwgoi sto neo meso
      do j = 1, 3
         k3_u(j) = accel(j)
         k3_r(j) = u(j)

         u(j) = u0(j) + k3_u(j)*dt         ! Kinisi sto telos tou diastimatos
         r(j) = r0(j) + k3_r(j)*dt
      enddo

      call calc_accel(u,Efield,Bfield,q,m,accel) ! Paragwgoi sto telos
      do j = 1, 3
         k4_u(j) = accel(j)
         k4_r(j) = u(j)
      enddo

c... Telika apotelesmata 
      do j = 1,3
         u(j) = u0(j) + (k1_u(j)+2D0*k2_u(j)+2D0*k3_u(j)+k4_u(j))*dt/6D0
         r(j) = r0(j) + (k1_r(j)+2D0*k2_r(j)+2D0*k3_r(j)+k4_r(j))*dt/6D0
      enddo
      return
      end

c=============================================
      real*8 function energy(r,u,Efield,q,m)
c=============================================
      implicit none
      integer j
      real*8 r(3), u(3)
      real*8 Efield(3), q, m
      real*8 ekin, edyn

      ekin = 0D0
      edyn = 0D0
      do j = 1, 3
         ekin = ekin + 0.5D0*m*u(j)*u(j)
         edyn = edyn + q*Efield(j)*r(j)
      enddo

      energy = ekin - edyn

      return
      end
