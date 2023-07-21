import java.util.ArrayList;

public class Calculus {


    public Calculus(){}


    public String derivitive(Double[] a){


        int b = a.length - 1;
        String answer = "";
        for(double x : a){
            double c = x*b;
            b-=1;
            if(b>-1) {
                answer += String.valueOf(c) + "x^" + String.valueOf(b) + " + ";
            }
            else{
                answer += String.valueOf(c) + "x^" + String.valueOf(b);
            }
        }

        return answer;
    }

    public Double[] derivitiveList(Double[] a){


        int b = a.length - 1;
        Double[] answer = new Double[a.length];
        for(int i = 0;i<a.length;i++){
            double c = a[i]*b;
            b-=1;
            answer[i] = c;
        }

        return answer;
    }

    public double derivitive(Double[] a, double b){


        int c = a.length - 1;
        double answer = 0;

        for(double x : a){
            answer += (x*b*c);
            c-=1;
        }

        return answer;

    }

    public String integral(Double[] a){

        int b = a.length;

        String answer = "";
        for(double x : a){
            double c = x/b;
            if(b>1) {
                answer += String.valueOf(c) + "x^" + String.valueOf(b) + " + ";
            }
            else{
                answer += String.valueOf(c) + "x^" + String.valueOf(b);
            }
            b-=1;
        }

        return answer;
    }

    public Double[] integralList(Double[] a){

        int b = a.length;

        Double[] answer = new Double[a.length];
        for(int i = 0; i<a.length;i++){
            double c = a[i]/b;
            answer[i] = c;
            b-=1;
        }

        return answer;
    }

    public double integral(Double[] a, double b, double c){


        int z = a.length;
        double answer = 0;

        for(double x : a){
            answer += ((Math.pow(b, z)) * (x/z)) - ((Math.pow(c, z)) * (x/z));
            z-=1;
        }
        return answer;
    }

  /*  public double arcLength(Double[] a, double b, double c){


        Double[] f = derivitiveList(a);
        //squaring polynomial
        ArrayList<Double> x= new ArrayList<Double>();
        int num = f.length;
        
        
        for(int i = 0; i<f.length; i++){
            
            for(int j = 0; j<f.length;j++){
                
            }
            
        }


    }

*/


}
