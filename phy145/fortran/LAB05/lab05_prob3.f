c=========================
      program resistance
c=========================
c xrisi function
c=========================
      real    Rtot, resist
      real    get_resistence
      integer J, Nres
      
      PRINT *,'***************************'
      PRINT *,'Praktiki me xrisi functions'
      PRINT *,'***************************'

      
      PRINT *, 'Eisagete tin timi tis antistasis'
      READ *, resist
      PRINT *, 'Eisagete to plithos twn antistasewn'
      READ *, Nres

      DO J =1, 2
         Rtot = get_resistence(Resist,Nres,J)
         if (j.eq.1) write(6,10)Rtot
         if (j.eq.2) write(6,11)Rtot
      ENDDO
 10   FORMAT(1x,'H oliki antistasi se syndesi kata seira einai Rtot =',
     &       1x,F10.2,1x,'Ohm')
 11   FORMAT(1x,'H oliki antistasi se parallili sundesi einai Rtot =',
     &       1x,F10.2,1x,'Ohm')
      END


c=============================================
      REAL FUNCTION GET_RESISTENCE(R,N,ITYPE)
c=============================================
c H parametros ITYPE kathorizei to eidos tou 
c ypologismou. Se seira ITYPE = 1 enw gia 
c parallili syndesi ITYPE = 2
c=============================================
      REAL R, RTOT
      INTEGER N, ITYPE, J

      RTOT = 0.           ! Arxiki timi gia ti synartisi
      DO J = 1, N
         IF (ITYPE .EQ. 1) THEN
            RTOT = RTOT + R
         ELSE IF (ITYPE .EQ. 2) THEN
            RTOT = RTOT + 1./R
         ENDIF
      ENDDO
      IF (ITYPE .EQ. 2) RTOT = 1./RTOT
c
      GET_RESISTENCE = RTOT   ! I synartisi exei pantote kapoia timi afou
                              ! Rtot pernei timii stin arxi aneksartita apo
                              ! tin timi tis metavlitis ITYPE
c
      RETURN
      END
