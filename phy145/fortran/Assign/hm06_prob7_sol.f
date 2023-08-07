c=============================
      program bars
c=============================
      implicit none
      integer iseed
      data iseed/123456/
      integer ntries, j, k
      integer nsuccess
      integer offside(6), ipos
      data offside/1,2,3,6,7,12/
      real r, probability

      call srand(iseed)
      print *,'Posa peiramata?'
      read *,ntries

      nsuccess = 0
      do j = 1, ntries
         ipos = 4
         do while (ipos.ne.11.and.ipos.ne.10)
            r = rand()
            if (r.lt.0.25) then                  ! Aristera
               ipos = ipos - 1
            elseif (r.lt.0.50) then              ! Deksia
               ipos = ipos + 1
            elseif (r.lt.0.75) then              ! Panw 
               if (ipos.lt.6) then
                  ipos = ipos - 3
               else
                  ipos = ipos - 4
               endif
            else                                 ! Katw
               if (ipos.gt.6) then
                  ipos = ipos + 3
               else
                  ipos = ipos + 4
               endif
            endif
            do k = 1, 6
               if (ipos.eq.offside(k)) goto 10
            enddo
         enddo
         nsuccess = nsuccess + 1
 10      continue
      enddo
      probability = float(nsuccess)/ntries
      write(6,20)ntries,nsuccess,probability*100
 20   format(1x,40('='),/,1x,'Arithmos peiramatwn:',3x,i7,/,
     &       1x,'Arithmos epityxiwn:',4x,I7,/,
     &       1x,'Pithanotita epityxias:',1x,F7.3,'%',/,
     &       1x,40('='))
      end
