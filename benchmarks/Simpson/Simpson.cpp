// numerical integration, simpson 1/3 method.
// Programmed by AKIYAMA M. on 2002-11-13.
double simpson( double f( const double ), const double a, const double b, int n ) {
	double h, sum_even, sum_odd;
	int even, odd;
	n=((n+1)/2)*2;
	h=(b-a)/n;
	sum_even=0;
	sum_odd=f(a+h);
	for ( even=2,odd=3; even<n; even+=2,odd+=2 ) {
		sum_even+=f(a+even*h);
		sum_odd+=f(a+odd*h);
	}
	return h*(f(a)+f(b)+2*sum_even+4*sum_odd)/3.0;
}

#include <cmath>
double func( const double x ) { return std::pow(x,4); }


#include <iostream>
#include <iomanip>
int main() {
	using namespace std;
    double a=0.0, b=1.0;
	for ( int n=2; n<=65536; n*=2) {
		double s=simpson( func, a, b, n );
		cout << "n=" << setw(6) << n 
			<< "  s=" << fixed << setprecision(16) << setw(20) << s << endl;
	}
}
