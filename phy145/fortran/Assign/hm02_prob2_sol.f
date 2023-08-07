      program ellipsis
c=====================================
c To programma ayto vriskei ola 
c ta simeia me akeraies syntetagmenes
c pou perikleiontai se mia elleipsi 
c=====================================
      implicit none
      integer jj,kk, npoints
      real    a, b, exiswsi
      print *,'Dwste to mikos tou kyriou aksona tis elleipsis [a]'
      read *,a
      print *,'Dwste to mikos tou deytereyonta aksona tis elleipsis [b]'
      read *,b

      npoints = 0
      write(6,10)a**2,b**2
      do jj = -int(a), int(a)
         do kk = -int(b), int(b)
            exiswsi = (jj/a)**2 + (kk/b)**2
            if (exiswsi.le. 1.0) then
               write(6,11)jj,kk
               npoints = npoints + 1
            endif
         enddo
      enddo
      write(6,12)npoints
 10   Format(1x,'Ta simeia me akeraies suntetagmenes pou periexontai',/,
     &       1x,'stin elleipsi x^2/',F3.0,'+y^2/',F3.0,'=1 einai:')
 11   Format(2x,'(',i2,',',1x,i2,1x,')')
 12   Format(1x,'Yparxoyn sunolika',i3,1x,'simeia')
      END
