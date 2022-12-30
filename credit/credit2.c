if (cn/pw(10,14) < 1)
    {
        long cnn = cn % pw(10,13);

        int k = 0;
        for (int i = 0; i < 6; i++)
        {
            k = k + (2 * (cnn - (cnn % pw(10, 12 - 2*i)))/pw(10, 12 - 2*i));
            printf("%i\n", k);
        }
    }
    else if (cn/pw(10,16) < 1)
    {
        long cnn = cn % pw(10,15);

        int k = 0;
        for (int i = 0; i < 7; i++)
        {
            k = k + (2 * (cnn - (cnn % pw(10, 12 - 2*i)))/pw(10, 12 - 2*i));
            printf("%i\n", k);
        }
    }
    else;
    {
        int k = 0;
        for (int i = 0; i < 9; i++)
        {
        k = k + (2 * (cn - (cn % pw(10, 2*i)))/pw(10, 2*i));
        printf("%i\n", k);
        }
    }