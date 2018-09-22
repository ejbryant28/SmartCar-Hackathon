const headers = new Headers({ Accept: 'application/json', 'Content-Type': 'application/json' });

export const login = () =>
  fetch('http://localhost:9090/login', {
    headers,
    body: JSON.stringify({
      //
    }),
  });
