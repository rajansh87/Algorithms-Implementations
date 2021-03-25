import java.io.*;
import java.util.*;

public class TestClass
{
	public static void main(String[] args) throws IOException 
	{
		BufferReader br=new BufferReader(new InputStreamReader(System.in));
		PrintWriter wr=new PrintWriter(System.out);
		String S=br.readLine();
		int N=Integer.parseInt(br.readLine().trim());
		String out_=solve(S,N);
		System.out.println(out_);
		wr.close();
		br.close();
	}
	static int [] compute_lps(String s)
	{
		int n=s.length();
		int [] lps=new int[n];
		int len=0;
		lps[0]=0;
		int i=1;
		while(i<n)
		{
			if(s.charAt(i)==s.charAt(len))
			{
				len++;
				lps[i]=len;
				i++;
			}
			else
			{
				if(len!=0)
				{
					len=lps[len-1];
				}
				else
				{
					lps[i]=0;
					i++;
				}
			}
		}
		return lps;
	}

	static String LongestSubstring(String s)
	{
		int [] lps=compute_lps(s);
		int n=s.length();
		if(lps[n-1]==0)
		{
			return("Go Away");
		}
		for(int i=0;i<n-1;i++)
		{
			if(lps[i]==lps[n-1])
			{
				return(s.substring(0,lps[i]));
			}
		}
		if(lps[lps[n-1]-1]==0)
		{
			return("Go Away");
		}
		else
		{
			return(s.substring(0,lps[lps[n-1]-1]));
		}
	}

	static String solve(String s,int n)
	{
		String st=LongestSubstring(s);
		int c=0,fromIndex=0;
		while((fromIndex=s.indexOf(st,fromIndex))!=-1)
		{
			c++;
			fromIndex++;
		}
		if(c>=n)
		{
			return st;
		}
		return("Go Away");
	}
}