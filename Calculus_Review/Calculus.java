import java.util.ArrayList;

//Function notation:
//[1, 2, 3] -> 1x^2 + 2x^1 + 3
//[2, 0, 5] -> 2x^2 + 5
//[9] -> 9

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


    public double areaBetweenCurves(Double[] topCurve, Double[] bottomCurve, double c, double d){


        int l1 = topCurve.length;
        int l2 = bottomCurve.length;

        int dif = l1-l2;


        if(dif>0){

            Double[] newList = new Double[topCurve.length];
            for(int i = 0;i< dif;i++){
                newList[i] = topCurve[i];
            }
            for(int i = 0;i< bottomCurve.length;i++){
                newList[i + dif] = topCurve[i + dif] - bottomCurve[i];
            }
            return -1 * integral(newList, c, d);
        }
        else if(dif<0){

            dif*=-1;
            Double[] newList = new Double[bottomCurve.length];
            for(int i = 0;i< dif;i++){
                newList[i] = bottomCurve[i];
            }
            for(int i = 0;i< topCurve.length;i++){
                newList[i + dif] = bottomCurve[i + dif] - topCurve[i];
            }
            return -1 * integral(newList, c, d);
        }
        else{

            Double[] newList = new Double[topCurve.length];

            for(int i = 0;i< newList.length;i++){
                newList[i] = topCurve[i] - bottomCurve[i];
            }
            return -1 * integral(newList, c, d);
        }



    }


    public double lRienmannSum(Double[] function, double start, double end, int intervals){


        Double[] range = new Double[intervals];
        double slope = (end-start) / intervals;

        for(int i = 0; i<range.length;i++){

            range[i] = start + i*slope;
        }

        double answer = 0;

        for(int i = 0; i<range.length;i++){

            for(int j = 0; j<function.length;j++){

                answer += function[j] * Math.pow(range[i], function.length - j - 1);
            }
        }

        return answer * slope;

    }


    public double rRienmannSum(Double[] function, double start, double end, int intervals){


        Double[] range = new Double[intervals];
        double slope = (end-start) / intervals;

        for(int i = 1; i<range.length+1;i++){

            range[i-1] = start + i*slope;
        }

        double answer = 0;

        for(int i = 0; i<range.length;i++){

            for(int j = 0; j<function.length;j++){

                answer += function[j] * Math.pow(range[i], function.length - j - 1);
            }
        }

        return answer * slope;

    }

    public double mRienmannSum(Double[] function, double start, double end, int intervals){

        Double[] range = new Double[intervals + 1];
        Double[] points = new Double[intervals];
        double slope = (end-start) / intervals;


        for(int i = 0; i<range.length;i++){
            range[i] = (i*slope);
        }

        for(int i = 0;i<points.length;i++){
            points[i] = (range[i+1] + range[i]) /2;
        }



        for(double x: range){
            System.out.println(x);
        }
        double answer = 0;

        for(int i = 0; i<points.length;i++){

            for(int j = 0; j<function.length;j++){

                answer += function[j] * Math.pow(points[i], function.length - j - 1);
            }
        }

        return answer * slope;

    }
    public double arcLength(Double[] a, double b, double c){

        //only works for f(x) = polynomial to the order of less than or equal to 2


        Double[] f = derivitiveList(a);


        //squaring polynomial list into new list


        if(f.length == 1){

            f[0] = Math.pow(f[0], 2);

            System.out.println(f[0]);
            f[0] += 1;

            System.out.println(f[0]);

            f[0] = Math.sqrt(f[0]);


            System.out.println(f[0]);

            return integral(f, c, b);
        }
        // add 1 to last term of new list

        //square root the new list

        // integral(newList, b,c)





        if(f.length == 2){
            double[] newList = new double[3];


            int count = 0;
            for(int i = 0;i<f.length;i++){

                for(int j = 0;j<f.length;j++){

                    if(count == 0){
                        newList[2] += f[i]*f[j];
                        count++;
                    }
                    else if(count ==1){
                        newList[1] += f[i]*f[j];
                        count++;
                    }
                    else{
                        newList[0] += f[i]*f[j];
                        count++;
                    }
                }
                count = 1;
            }

            newList[2] +=1;

            for(int i = 0;i< newList.length;i++){
                newList[i] = Math.sqrt(newList[i]);
            }

            Double[] g = new Double[3];
            for(int i = 0;i<g.length;i++){
                g[i] = newList[i];

            }
            return integral(g, c, b);
        }

        if(f.length == 3) {
            //doesn't work corrrectly: can't take square root of polynomial


            double[] newList = new double[3];


            int count = 0;
            for (int i = 0; i < f.length; i++) {

                for (int j = 0; j < f.length; j++) {

                    if (count == 0) {
                        newList[0] += f[i] * f[j];
                        count++;
                    } else if (count == 1) {
                        newList[1] += f[i] * f[j];
                        count++;
                    } else {
                        newList[2] += f[i] * f[j];
                        count++;
                    }
                }
                count = 1;

            }


            newList[2] += 1;

            for(double x: newList){
                System.out.println(x);
            }

            for (int i = 0; i < newList.length; i++) {
                newList[i] = Math.sqrt(newList[i]);
            }

            Double[] g = new Double[3];
            for (int i = 0; i < g.length; i++) {
                g[i] = newList[i];

            }
            return integral(g, c, b);

        }
        return 0.0;

    }






}
