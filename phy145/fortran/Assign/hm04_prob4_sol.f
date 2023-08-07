      program capacitor_Efield
c==========================================
c To programma lunei tin eksiswsi Laplace
c gia tin periptwsi enos epipedou puknwti
c me tin methodo twn stoixeiwdwn diaforwn
c==========================================
      implicit none
      integer irow, icol
      integer nrow, ncol
      parameter(nrow=101,ncol=101)
      integer iter, mxiter, iterfin
      parameter(mxiter=1000)
      integer posirow, posicol1, posicol2
      integer negirow, negicol1, negicol2
      parameter(posirow=13,posicol1=20, posicol2=80)
      parameter(negirow=26,negicol1=20, negicol2=80)
      real*8 V(nrow,ncol)
      real*8 V_iter(nrow,ncol),V_trace(nrow,ncol)
      real*8 trace, tracedif, trace_prev
      real*8 precision
      real*8 tracefin, diffin
      parameter(precision=1.0D-6)
      logical posplate, negplate
      logical tracedone,iterdone
c
c...Prosdiorismos sunoriakwn sunthikwn
c======================================
      trace = 0.0d0
      do irow=1, nrow
         do icol=1, ncol
            V(irow,icol) = 0.0d0         !<< Ola ta simeia me dunamiko 0
            if (irow.eq.posirow) then    !<< Epipedo puknwti me dynamiko +100V
               if (icol.ge.posicol1.and.icol.le.posicol2) then
                  V(irow,icol)=100.0d0
               endif
            endif
            if (irow.eq.negirow) then    !<< Epipedo puknwti me dunamiko -100V
               if (icol.ge.negicol1.and.icol.le.negicol2) then
                  V(irow,icol)=-100.0d0
               endif
            endif
            if (irow .eq. icol) trace = trace+abs(V(irow,icol))
         enddo
      enddo
c
c Efarmogi tis methodou eksisorropisis
c======================================
      iter = 0
      tracedif = 1.0d0
      tracedone  = .false.
      iterdone   = .false.
      do while (tracedif.gt.precision)
         trace_prev = trace
 100     iter=iter+1
         trace = 0.0d0
         do irow=2, nrow-1      !<< Oi perifereiakes plegmatikes grammes
            do icol=2, ncol-1   !<< einai pantote geiwmenes (V=0)
               posplate = irow.eq.posirow .and.
     &                    (icol.ge.posicol1.and.icol.le.posicol2)
               negplate = irow.eq.negirow .and.
     &                    (icol.ge.negicol1.and.icol.le.negicol2)
               if ( posplate ) then 
                  V(irow,icol) = 100.0d0
               else if ( negplate ) then
                  V(irow,icol) = -100.0d0
               else
                  V(irow,icol) = V(irow,icol-1)+V(irow,icol+1) + 
     &                           V(irow-1,icol)+V(irow+1,icol)
                  V(irow,icol) = V(irow,icol)/4.d0
               endif
               if ((icol.eq.irow).and..not.tracedone) then
                  trace = trace + abs(V(irow,icol))
               endif
            enddo
         enddo
         tracedif = abs((trace-trace_prev)/trace_prev)
         if ((tracedif.lt.precision).and..not.tracedone) then
            tracedone = .true.
            tracefin = trace
            diffin   = tracedif
            iterfin  = iter
            do irow=1,nrow
               do icol=1,ncol
                  V_trace(irow,icol) = V(irow,icol)
               enddo
            enddo
         endif
         if ((iter.eq.mxiter).and..not.iterdone) then
           iterdone = .true.
           do irow=1,nrow
              do icol=1,ncol
                 V_iter(irow,icol) = V(irow,icol)
              enddo
           enddo
        endif
        if (tracedone.and..not.iterdone) goto 100  !<< se periptwsi pou exoume
                                                   !<< tin epithymiti akriveia
                                                   !<< apo ton elegxo tou trace
                                                   !<< alla den exoume itermax
      enddo
 101  continue
      open(unit=30,file='hm04_prob4_iter.dat',status='unknown')
      open(unit=31,file='hm04_prob4_trac.dat',status='unknown')
      do irow=1, nrow
         do icol=1, ncol
            write(30,*)irow,icol,V_trace(irow,icol)
            write(31,*)irow,icol,V_iter(irow,icol)
         enddo
         write(30,*)    !<< Mia keni grammi gia na ksexwrisoun ta blocks
         write(31,*)    !<< kai na ginei kalytera to grafima sto gnuplot
      enddo

      close(30)
      close(31)
      end
