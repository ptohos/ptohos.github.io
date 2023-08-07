#!/usr/bin/python3

'''============================================================================
... Efarmogi tis methodou Runge-Kutta 4-is taksis gia tin perigrafi tis
... kinisis enos swmatos se reusto katw apo tin epidrasi mias dunamis 
... antistasis analogis tis taxutitas tou swnatos se kapoia dynami. 
... Efarmogi tis methodou gia tin periptwsi tis katakoryfis volis enos
... swmatos.  
...
... To programma perissotero deixnei to tropo xrisis tis methodou 
... Runge-Kutta kai ta diafora vimata pou prepei na akolouthithoun.
...
... To systima perigrafetai apo 2 diaforikes eksiswseis 1-is taksis
... (gia taxutita kai thesi) sti y-dieythinsi. An eixame kinisi se 
... 2-diastaseis (p.x. plagia voli) tha eixame 4 diaforikes eksiswseis.
... Epomenws kathe fora prepei na ypologisoume 2 paragwgous.
... H mia einai i epitaxunsi kai epireazei tin ekseliksi tis taxutitas 
... kai i alli einai i taxutita pou epireazei tin ekseliksi tis thesis.
...
... Arxika as doume theoretika to xrono anodou kai kathodou
... katw apo tin epidrasi tis dunamis tis antistasis:
...
... Stin periptwsi ayti i mixaniki energeia toy swmatos den diatireitai
... logw tis antistasis toy aera. Wstoso i dynamiki energeia einai i idia
... se kathe simeio tis troxias (eite to swma anevainei eite katevainei). 
... Alla i kinitiki tou energeia einai megaluteri kathws anevainei se sxesi
... me ayti poy exei sto idio upsos otan katevainei. Ayto symvainei epeidi
... i antistasi tou aera exei energisei se megalyteri diadromi:
....
... DeltaE_mix = -E_kin^an - E_dyn^an + E_kin^kat + E_dyn^kat = -W_aera =>
... W_aera = 0.5*m*(u_kat^2 - u_an^2) => u_kat - u_an < 0 => u_kat < u_an
...
... opou E_kin^an, E_kin^kat, E_dyn^an, Edyn^kat einai oi kinitiki kai
... dynamiki energeia tou swmatos otan anevainei kai otan katevainei. 
...
... H taxytika me tin opoia katebainei to swma einai se kathe simeio tis
... troxias mikroteri apo tin taxytita tou swmatos sto antistoixo simeio
... otan to swma anevainei. Etsi otan to swma ftasei sto edafos tha exei
... mikroteri taxytita apo tin taxytita pou eixe otan ektokseythike.
... H mesi taxytita anodou einai:   <u>^an = hmax/t_an
... H mesi taxytita kathodoy einai: <u>^kat = hmax/t_kat
... H taxytita stin anodo metavaletai apo u0 -> 0 enw stin kathodo apo 0->u0'
... opou u0' < u0 symfwna me ta parapanw. Epomenws kai <u>^kat < <u>^an. 
... Afou to hmax einai idio kai stis 2 periptwseis tote
... 1/t_an > 1/t_kat => t_kat > t_an.
...
... Enas diaforetikos sulogismos einai me vasi tis dynameis. Kathws to swma
... anevainei dexetai synoliki dunami 
... Fol_an  = F_var + F_ant enw otan katevainei i dynami 
... Fol_kat = F_var - F_ant. 
... Epomenws to swma dexetai megalyteri epitaxynsi otan anevainei apo otan
... katevainei kai ara stamata pio grigora. 
...
... Epomenws perimenoume lunontas to provlima na vroume oti o xronos kathodou
... einai megalyteros apo ton xrono anodou. 
    ========================================================================='''
 
import numpy as np
import matplotlib.pyplot as plt

def dydt(t,y,v):
    '''==============================
       H paragwgos dy/dt = v_y
       =============================='''
    d1dt_coord = v
    return d1dt_coord
    
def dvdt(t,y,v):
        ''' ============================================
            H paragwgos d^2y/dt^2 = dv_y/dt = accel_y
            H parakatw periptwsi einai gia F_ant =-Dv^2
            Gia F_ant = -Dv 
                d2y = -1.0 * ( g + D * y(2) )
            Gia F_ant = -Dv^3
                d2y = -1.0 * ( g + D * v^2 * y(2) )
           ============================================='''
        vel_magnitude = abs(v)
        d2dt_coord = -g - Drag * v * vel_magnitude
        return d2dt_coord

def rk4(t_i,t_f,y_i,v_i):
    '''====================================
        Runge-Kutta 4th-order
       ====================================
       Orismata eisagwgis tis methodou:
          t_i:   arxi tou ypodiastimatos 
          t_f:   telos toy ypodiastimatos
          y_i:   arxiki thesi ti xroniki stigmi t_i
          v_i:   arxiki taxutita ti xroniki stigmi t_i
       H methodos epistrefei:
          y_f:   teliki thesi ti xroniki stigmi t_f
          v_f:   teliki taxytita ti xroniki stigmi t_f 
       ===================================='''

    h = t_f - t_i    # Euros diastimatos tis aneksartitis metavlitis
    hh = h/2         # Miso diastima
    t  = t_i
    
    ''' Ypologismos tou k1 '''
    k1y = dydt(t,y_i,v_i)   # Paragwgoi thesis kai taxutitas stin
    k1v = dvdt(t,y_i,v_i)   # arxi tou xronikou diastimatos

    ''' Ypologismos tou k2 '''
    k2y = dydt(t+hh, y_i + k1y*hh, v_i + k1v*hh) # Miso vima Euler gia thesi
    k2v = dvdt(t+hh, y_i + k1y*hh, v_i + k1v*hh) # Miso vima Euler gia taxutita

    ''' Ypologismos tou k3 '''
    k3y = dydt(t+hh, y_i + k2y*hh, v_i + k2v*hh) # Miso vima Euler gia thesi
    k3v = dvdt(t+hh, y_i + k2y*hh, v_i + k2v*hh) # Miso vima Euler gia taxutita

    ''' Ypologismos tou k4 '''
    k4y = dydt(t+h, y_i + k3y*h, v_i + k3v*h) # Olokliro vima Euler sto telos
    k4v = dvdt(t+h, y_i + k3y*h, v_i + k3v*h) # tou xronikou diastimatos

    ''' Efoson exoume vrei tis 8 paragwgous 
        (4 gia thesi kai 4 gia taxutita) 
        efarmozoume sto teliko apotelesma '''
    y_f = y_i + (k1y + 2*k2y + 2*k3y + k4y) * h/6.
    v_f = v_i + (k1v + 2*k2v + 2*k3v + k4v) * h/6.

    return y_f, v_f


def interpolate(x0,x1,y0,y1,yfin):
    '''==============================================================
       Dinontas tis suntetagmenes 2 simeiwn A(x0,y0) kai B(x1,y1)
       xrisimopoioume tin eksiswsi tis eytheias pou perna apo ta
       2 simeia gia na broume tin x i tin y syntetagmeni enos tritou 
       simeiou pou vrisketai stin eytheia kai tou opoiou kseroume
       tin mia apo tis 2 syntetagmenes
       ==============================================================
       Stin prokeimeni periptwsi xrisimopoioume ti grammiki paremvoli
       gia 2 periptwseis. Gia na vroume to xrono anodou/kathodou me 
       vasi tin taxutita kai gia na vroume to megisto upsos me vasi
       tin taxytita. Epomenws ta simeia mas tha exoun suntetagmenes
       t kai u stin 1-i periptwsi kai h kai u sti 2-i periptwsi.
       Epomenws to rolo tis x metavlitis paizei o xronos t
       kai to rolo tis y metavlitis i taxytita tou swmatos (1-periptwsi)
       enw to rolo tis x metavlitis sti 2-i periptwsi paizei 
       i thesi tou swmatos kai tis y metavlitis i taxytita.  
      =============================================================='''
    xfin = x0 + (x1 - x0) * (yfin-y0) / (y1-y0)
    return xfin


def main():
    global g, Drag       # Kanoume tis 2 metavlites global
    y_init = float(input("The initial position of the object [y_init=0] "))
    v_init = float(input("The initial velocity of the object [v_init=50] "))
    mass   = float(input("The mass of the object [mass=1E-2] "))
    Drag   = float(input("The drag coefficient [Drag = 1E-2] "))
    dt     = float(input("The time step [dt=0.01] " ))

    g       = 9.81
    t_init  = 0.0
    time    = 0.0
    y_0     = y_init
    ypos    = y_init
    velo    = v_init

    Velocity, YPosition = [], []
    Time, Energy = [], []
    Force = []

    # H arxiki energeia toy vlimatos E0
    E0 = mass * (g * ypos + 0.5 * velo**2)
    E = E0

    # H dunami pou dexetai arxika to swma
    F = -mass * (g + Drag * velo * abs(velo))

    KeepLooping = True

    while KeepLooping:
        Time.append(time)
        Velocity.append(velo)
        YPosition.append(ypos)
        Force.append(F)
        Energy.append(E/E0)

        # Epomeni xroniki stigmi 
        t_init  = time
        time    = t_init + dt
        y_init  = ypos
        v_init  = velo

        #========================
        # Klisi tis methodou RK4
        #========================
        ypos,velo = rk4(t_init,time,y_init,v_init)

        # Energy
        E = mass * (g * ypos + 0.5 * velo**2)

        # Force
        F =  -mass * (g + Drag * velo * abs(velo))

        # Elegxos gia to an to swma eftase sto megisto upsos
        if (v_init * velo < 0) :        # H taxytita allazei prosimo
            t_ano  = interpolate(t_init, time, v_init, velo, 0.0)
            h_max  = interpolate(y_init, ypos, v_init, velo, 0.0)

        # Elegxos gia to an to swma epestrepse sto arxiko upsos
        if (ypos < 0.0) :
            KeepLooping = False

    #  Euresi tou olikou xronou
    t_ol = interpolate(t_init, time, y_init, ypos, 0.0)
    t_kat = t_ol - t_ano
    print(55*('='))
    print(' O xronos anodou einai: \t\t %8.4f (s)' % (t_ano))
    print(' O xronos kathodou einai: \t\t %8.4f (s)' % (t_kat))
    print(' To megisto upsos tis troxias einai: \t %8.4f (m)' % (h_max))
    print(55*('='))

    plt.figure(figsize=(8,5))
    plt.plot(Velocity,Force,'k-')
    plt.xlabel('Velocity m/s')
    plt.ylabel('Force (N)')
    plt.grid(True)
    plt.show()
    
main()
