Attached please find two files, 
plotcomp09-Kerzendorf02.cps and plotcomp09-Kerzendorf02.dat,
which are for the Han 2008 paper. 
(In the paper, we adopted alpha_CE=alpha_th=1.)
plotcomp09-Kerzendorf02.cps is for the distributions of properties, 
while plotcomp09-Kerzendorf02.dat is for the data extracted.

The data file is written with the following FORTRAN statements,
      do i=1,ns
         write(91,19) m1f(i), teff(i), l(i), grav(i), vrot(i), vr(i),
     &               vwd(i), periodf(i), a(i), ar(i), dmt1(i), wind(i)
 19      format(1x, 12(f8.4,1x))
while ns is the number of data points (55345 actually).

m1f: companion's mass (in solar) at the moment of SN explosion,
teff: companion's effective temperature (in log10(Teff/K)) at the 
      moment of SN explosion,
l: companion's luminosity (in log10(L/Lsun)) at the moment of SN explosion,
grav: companion's surface gravity (in log10(g/cm s^-2)) at the moment of
       SN explosion,
vrot: companion's equatorial rotational velocity (in km/s) at the moment
       of SN explosion,
vr: companion's orbital velocity (in km/s) at the moment of SN explosion,
vwd: WD's orbital velocity (in km/s) at the moment of SN explosion,
periodf: orbital period (and also the rotational period of the companion,
        as corotation is very likely) of the WD+MS system at the moment
        of SN explosion (in log(P/days)),
a: orbital separation (in solar radius) of the binary system at the moment
        of SN explosion,
ar: the ratio of orbital separation to companion's radius at the moment of
        SN explosion,
dmt1: mass tranfer rate (in log(-dM/dt /Msun yr^-1)) at the moment of SN 
      explosion,
wind: mass lost during optically thick stellar wind phase (in solar).


