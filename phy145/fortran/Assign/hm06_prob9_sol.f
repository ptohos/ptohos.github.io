      program randomwalkcube
      implicit none
      
      integer iexp, iseed
      data iseed/12345/
      integer b1, b2, b3, s0
      integer ab1, ab2, ab3
      integer b1_node, b2_node, b3_node
      integer Nexp, nsteps, nsteps_tot
      integer iexp2print
      real    p, q, r, tot_prob, test, mean_time
      
      
 10   Print*,'Dose to S0, tis pithanotites kai to sunolo twn peiramatwn'
      read*,s0,p,q,r, Nexp
      tot_prob = p+q+r
      if (tot_prob.ne.1) then 
         print *,'H oliki pithanotita metavasis den einai 1'
         print *,'Exetaste tis pithanotites poy dwsate'
         goto 10
      endif
      print*,'Poses diadromes na typwsei?'
      read*, iexp2print

      call findbits(s0,b1,b2,b3)
      
      ab1=abs(b1-1)    ! Ta bits tis korufis tou proorismou
      ab2=abs(b2-1)
      ab3=abs(b3-1)

      b1_node = b1     ! Kratame ta bits tis korufis pou ksekina (arxiki 
      b2_node = b2     ! synthiki) wste na ta xrisimopoioume se kathe 
      b3_node = b3     ! neo peirama iexp pou eksetazoume

      nsteps_tot = 0   ! O metritis twn sunolikwn diadromwn gia ola
                       ! ta peiramata Nexp pou tha dokimasoume
      call srand(iseed)
      Do iexp = 1, Nexp
c...  
         nsteps  = 0   ! Midenismos twn arithmwn twn vimatwn tis diadromis
         b1 = b1_node  ! Kathe epanalipsi diadromis prepei na ksekina
         b2 = b2_node  ! apo tin idia arxiki katastasi twn bits
         b3 = b3_node  ! Opote antikatastoume ta bits tis arxikis katastasis
c...
         Do while((b1.ne.ab1).or.(b2.ne.ab2).or.(b3.ne.ab3))
            if (iexp .le. iexp2print) then 
               call nodeprint(b1,b2,b3) ! Endiameses koryfes
            endif
            test = rand()
            if (test .le. p) then
               b1 = abs(b1-1)
            else if(test .le. (p+q)) then
               b2 = abs(b2-1)
            else
               b3 = abs(b3 - 1)
            endif
            nsteps = nsteps + 1
         Enddo
         if (iexp .le. iexp2print) then 
            call nodeprint(b1,b2,b3) ! H epithymiti koryfi proorismou
            write(6,*)
         endif
         nsteps_tot = nsteps_tot + nsteps
      Enddo
      
      Mean_time = float(Nsteps_tot)/float(Nexp)
      Write(6,20) Nexp, Mean_time
 20   Format(1x,65('='),/,2x,'O mesos xronos antikoryfis meta apo',
     &       1x,I7,1x,'dokimes einai:',1x,F4.1,/,1x,65('='))
      End

c===================================================
      subroutine findbits(igive,ibit1,ibit2,ibit3)
c===================================================
      implicit none
      integer igive
      integer ibit1, ibit2, ibit3
      
      ibit1 = igive/100
      ibit2 = mod(igive,100)/10
      ibit3 = mod(igive,2)
      return
      end

c==================================================
      subroutine nodeprint(ibit1,ibit2,ibit3)
c==================================================
      implicit none
      integer ibit1,ibit2,ibit3
      character*3 node
      character*1 ch1,ch2,ch3
      
      write(ch1,10)ibit1    ! Ayto einai ena trick gia na typwsoume
      write(ch2,10)ibit2    ! akeraious san characters stin Fortran
      write(ch3,10)ibit3    ! Kapoios tha mporouse na grapsei tin korufi
 10   format(I1)            ! san 3bits sunexomena, diladi na dwse
      node = ch1//ch2//ch3  !    write(6,30)ibit1,ibit2,ibit3
      write(6,20)node       ! 30 format(2x,I1,I1,I1)
 20   format(2x,A3)         ! pou einai pio eukolo alla sas dinw ena kalutero
      return                ! tropo pou mporei na xrisimopoiithei kai allou.
      end                   ! Kapoioi tha to proseksan se kapoia lusi apo ta
                            ! homeworks
