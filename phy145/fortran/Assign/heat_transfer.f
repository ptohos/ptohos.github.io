c===========================
      program heat_transfer
c===========================
      implicit none
      integer imax, jmax
      integer itmax
      parameter(imax    = 100)
      parameter(jmax    = 100)
      real*8  heat(imax,jmax)
      real*8  epsi, diff
      integer nrow, ncol, niter, nreport
c
      call initialize(heat,nrow,ncol,epsi,itmax,nreport)

      call calculate(heat,nrow,ncol,epsi,itmax,nreport)

      end

c================================================================
      subroutine calculate(heat,nrow,ncol,epsi,itmax,nreport)
c================================================================
      implicit none
      logical notdone
      integer count, i, j
      integer nrow, ncol
      integer icent, jcent
      integer imax, jmax
      integer itmax, nreport
      parameter(imax    = 100)
      parameter(jmax    = 100)
      real*8  heat(imax,jmax)
      real*8  oldheat(imax,jmax)
      real*8  epsi, tcenter, oldtcenter
      real*8  refdiff, diff
      character*30 form

      open(unit=60,file='heat.out',status='unknown')
      
      notdone = .true.
      count = 0
      icent = nrow/2 + 1
      jcent = ncol/2 + 1
      do while (notdone .and. count .le. itmax)

         do i = 2, nrow-1
            do j = 2, ncol-1
               oldheat(i,j) = heat(i,j)
               heat(i,j) = 0.25*(heat(i-1,j)+heat(i+1,j)+
     &                           heat(i,j-1)+heat(i,j+1))
            enddo
         enddo

         oldtcenter = oldheat(icent,jcent)
         tcenter = heat(icent,jcent)
         diff = dabs(oldtcenter - tcenter)
         refdiff = dabs(tcenter - 175.0d0) 
         if (refdiff.lt.epsi) notdone = .false.

         if (notdone) then 
            count = count + 1
            if (mod(count,nreport).eq.0) then 
               write(6,10)count,diff,tcenter,refdiff
            endif
         endif
      enddo
 10   format(1x,'Meta apo',1x,I5,
     &       1x,'sarwseis i metaboli sto kentro einai',1x,f6.2,/,
     &       1x,'H thermokrasia tou kentrikou simeiou einai',1x,f6.2,/, 
     &       1x,'me diafora apo 175C isi me:',1x,f6.2,/)
      
c===========
c Print out
c===========
      call makeformat(ncol,form)

      if (count.lt.itmax) then 
         write(6,20)count,tcenter
         do i = 1, nrow
            write(60,form)(heat(i,j),j=1,ncol)
         enddo
      else
         write(6,21)
      endif
 20   format(1x,80('='),/,
     &       1x,'Thermiki isorropia meta apo',1x,I5,1x,'sarwseis',/,
     &       1x,'Thermokrasia kentrikou plegmatikou simeiou:',1x,f6.2,/,
     &       1x,80('='))
 21   format(1x,'Arithmos sarwsewn jeperase to max orio')
      close(50)
      return
      end

c================================================================
      subroutine makeformat(ncol,form)
c================================================================
c Kataskeyi metablitou format
c================================================================
      implicit none
      integer nrow,ncol
      character*(*) form
      character*3 fm1, fm2

      if (ncol.lt.10)then
         write(fm1,10)ncol
      else if (ncol.lt.100) then
         write(fm1,11)ncol
      else
         write(fm1,12)ncol
      endif
      form = '('//fm1//'(1x,f6.2))'
 10   format(i1)
 11   format(i2)
 12   format(i3)
      return
      end

c================================================================
      subroutine initialize(heat,nrow,ncol,epsi,itmax,nreport)
c================================================================
      implicit none
      integer i, j
      integer nrow, ncol
      integer imax, jmax
      integer itmax, nreport
      parameter(imax    = 100)
      parameter(jmax    = 100)
      real*8  heat(imax,jmax)
      real*8  epsi
      real*8  temp1, temp2, temp3, temp4
      character*2 fm1, fm2
      character*50 form1, form2
      character*70 form3

 10   print *,' Give the number of the horizontal lines'
      read *,nrow
      if (nrow.gt.imax) then 
         print *,' Arithmos horizantal lines',nrow,'> imax=',imax
         print *,' Please reduce the number '
         goto 10
      endif
 11   print *,' Give the number of the vertical lines'
      read *,ncol
      if (ncol.gt.jmax) then 
         print *,' Arithmos vertical lines',ncol,'> jmax=',jmax
         print *,' Please reduce the number '
         goto 11
      endif

      print *,' Give the desired tollerance epsilon'
      read *,epsi

      print *,' Give the maximum number of iterations'
      read *,itmax

      print *,' Give the number of iteration for reporting'
      read *,nreport

      print *,' Give the Temperature of the boundary lines'
      print *,' Top horizonal surface Temperature >'
      read *,temp1
      print *,' Bottom horizontal Temperature >'
      read *,temp2
      print *,' Left vertical Temperature >'
      read *,temp3
      print *,' Right vertical Temperature >'
      read *,temp4
c
c Initialization of the heat matrix and boundary temperatures
c=============================================================
      do i = 1, imax
         do j = 1, jmax
            if (i.eq.1) then 
               heat(i,j) = temp1
            else if (j.eq.1) then 
               heat(i,j) = temp3
            else if (j.eq.ncol) then
               heat(i,j) = temp4
            else if (i.eq.nrow) then
               heat(i,j) = temp2
            else
               heat(i,j) = 0.0d0
            endif
         enddo
      enddo
c 
c Print out the initial conditions 
c==================================
      if (ncol.le.10) then 
         write(fm1,50)ncol-1
         write(fm2,50)ncol-3
      else if (ncol.le.100) then
         write(fm1,51)ncol-1
         write(fm2,51)ncol-3
      endif
 50   format(i1)
 51   format(i2)
      form1 = '(1x,I4,'//fm1//'(5("-"),I3),/,3x,"|",'
     &        //fm1//'(7x,"|"))'
      form2 = '(1x,I4,'//fm1//'(5("-"),I3),/)'
      form3 = '(1x,I4,6("-"),I1,'//fm2//'(7("-"),I1),'
     &         //'6("-"),I3,/,3x,"|",'//fm1//'(7x,"|"))'
      write(6,52)nrow, ncol, itmax, epsi
      do i = 1, nrow
         if (i.eq.1) then 
            write(6,form1)(int(heat(i,j)),j=1,ncol)
         else if (i.eq.nrow) then 
            write(6,form2)(int(heat(i,j)),j=1,ncol)
         else
            write(6,form3)(int(heat(i,j)),j=1,ncol)
         endif
      enddo
 52   format(1x,80('='),/,1x,'Arithmos plegmatikwn grammwn',1x,i3,/,
     &       1x,'Arithmos plegmatikwn stilwn',1x,i3,/,
     &       1x,'Megistos arithmos apaitoumenwn epanalipsewn',1x,i5,/,
     &       1x,'Gia epiteuksi akriveias epsilon',1x,f4.2,/,80('='),/,
     &       1x,'Oi arxikes sunthikes toy problimatos einai:',/)
      
      return
      end
