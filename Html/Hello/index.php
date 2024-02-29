<!DOCTYPE html>
<html>
<head>
    <title>PHP Request</title>
</head>
<body>

<div id="response">
    <?php
    $url = 'https://vaprevention.rd.ciencias.ulisboa.pt/kJ353HI8dejs8/proj/avaliacao/ChatBotClassRedesign/Html/Hello/MiddleWare.py';
    $options = array(
        'http' => array(
            'header'  => "Content-type: application/json\r\n",
            'method'  => 'GET',
        )
    );
    $context  = stream_context_create($options);
    $response = file_get_contents($url, false, $context);

    if ($response !== false) {
        echo $response;
    } else {
        echo "Error: Failed to fetch data";
    }
    ?>
</div>

</body>
</html>


<!DOCTYPE html>
<html>
<head>
    <title>PHP Request</title>
</head>
<body>

<div id="response">
    <?php
    $response = file_get_contents('http://127.0.0.1:5000/testeHello');
    if ($response !== false) {
        $data = json_decode($response, true);

        if (isset($data['message'])) {
            echo $data['message'];
        } else {
            echo $response;
        }
    } else {
        echo "Error: Failed to fetch data";
    }
    ?>
</div>

</body>
</html>
