package Main;
import java.util.Scanner;

public class Main {
	static int[] sorted;
	static int K;
	static int cnt;
	static int ans = -1;
	public static void main(String[] args) {	
		Scanner sc = new Scanner (System.in);
		int N = sc.nextInt();
		K = sc.nextInt();
		sorted = new int[N];
		int a[] = new int[N];
		for (int i =0;i<N;i++) {
			a[i] = sc.nextInt();
		}
		sc.close();
		mergesort(a,0,N-1);
        System.out.println(ans);
	}
	
	public static void merge(int a[],int start,int mid,int end) {
		int i = start;
		int j = mid + 1;
		int k = 0;
		
		while (i <= mid && j<=end) {
			if (a[i] <= a[j]) {
				sorted[k] = a[i];
				i++;
			}else {
				sorted[k] = a[j];
				j++;
			}
			k++;
		}
        while (i <= mid) {
            sorted[k] = a[i];
            i++;
            k++;
        }
        while (j <= end) {
            sorted[k] = a[j];
            j++;
            k++;
        }
        k = 0;
        i = start;
        
        while (i<=end) {
        	cnt ++;
        	if (cnt == K) {
        		ans = sorted[k];
        		break;
        	}
        	a[i] = sorted[k];
        	i++;
        	k++;
        }
	}
	public static void mergesort(int a[],int start,int end) {
		if (start < end) {
			int mid = (start + end)/2;
			mergesort(a,start,mid);
			mergesort(a,mid+1,end);
			merge(a,start,mid,end);
		}
	}
}