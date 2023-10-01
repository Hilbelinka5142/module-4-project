
<!DOCTYPE html>
<html>
<head>
    <title>Module 4 project</title>
</head>
<body>
    <h1>Hello {
    from requests import get
    ip = get('https://api.ipify.org').text
    print('My public IP address is: {}'.format(ip))}</h1>
</body>
</html>
