      Program randomwalk2d
      implicit none
      integer iseed
      data iseed/12345/
      Integer xpos, ypos
      Integer xuplim, xlolim
      Integer yuplim, ylolim
      parameter(xuplim = 8)
      parameter(xlolim = 1)
      parameter(yuplim = 8)
      parameter(ylolim = 1)
      Integer iwalk, nwalks
      Integer nstp, maxsteps, minsteps
      Integer dist
      Real R

      call srand(iseed)
      dist = 0

      nwalks = 5000         ! Megistos arithmos petyximenwn prospatheiwn
      Do iwalk = 1, nwalks
        xpos = xuplim       ! Simeio ekkinisis - Estw i panw deksia gwnia
        ypos = yuplim       ! Simeio ekkinisis - Estw i panw deksia gwnia

        nstp = 0
1       Nstp = nstp + 1
        R=Rand()            ! Enas tyxaios arithmos sto [0,1)
        
c... Yparxoun 4 dunates periptwseis gia na kinithei: deksia/aristera/panw/katw
c... Oi 4 periptwseis einai isopithanes, kathe mia 0.25 
        If (R .gt. 0.75) then
           xpos = xpos + 1               ! Tha kineithei sta deksia
        endif
        iF  ((R .gt. 0.5) .and. (R .lt. 0.75)) then
           xpos = xpos - 1               ! Tha kineithei aristera
        endif
        iF  ((R .gt. 0.25) .and. (R .lt. 0.5)) then
           ypos = ypos - 1               ! Tha kineithei katw
        endif
        If (R .lt. 0.25) then
           ypos = ypos + 1               ! Tha kineithei panw
        endif
        
c... Elegxos gia to an to vima pou kanei einai entos i ektos oriwn plegmatos.
c... An einai ektos oriwn, epistrefoume stin arxiki thesi prin to vima kai 
c... elattwnoume ton arithmo twn vimatwn kata 1 wste na ksanaprospathisoume
        If (xpos .gt. xuplim) then
          xpos = xpos - 1
          nstp = nstp - 1
        endif
        If (ypos .gt. yuplim) then
          ypos = ypos - 1
          nstp = nstp - 1
        endif
        If (xpos .lt. xlolim) then
          xpos = xpos + 1
          nstp = nstp - 1
        endif
        If (ypos .lt. ylolim) then
          ypos = ypos + 1
          nstp = nstp - 1
        endif
        
c... Den ftasame sti katw aristeri gwnia opote sunexizoume ta vimata
        If ((xpos .ne. xlolim) .OR. (ypos .ne. ylolim)) then
           goto 1
        endif

c... Eyresi tou megistou kai elaxistou arithmou vimatwn
c... anamesa stis mexri twra epitixeis diadromes
        if (iwalk .eq. 1) then 
           maxsteps = nstp
           minsteps = nstp
        elseif (maxsteps .lt. nstp) then
           maxsteps = nstp
        elseif (minsteps .gt. nstp) then
           minsteps = nstp
        endif
        
        dist = dist + nstp
      enddo
      print*,"====== Apotelesmata meta apo ",nwalks," diadromes ======"
      Print*,"Diadromi me max vimata = ",maxsteps
      Print*,"Diadromi me min vimata = ",minsteps
      Print*,"Mesi timi diadromis    = ",dist/float(nwalks)
      end
