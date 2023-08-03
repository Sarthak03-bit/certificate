import pdfkit


def generate_certificate(name, course, date):
    html_content = """
  <style type="text/css">
    body,
    html {
      margin: 0;
      padding: 0;
    }

    body {
      color: black;
      font-family: Verdana, Helvetica;
      text-align: center;
    }

    .container {
      border: 20px solid #524fff;
      width: 1151px;
      height: 802px;
    }

    .wrapper {
      text-align: center;
      height: 500px;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .logo-wrapper {
      width: 100%;
      display: flex;
      justify-content: center;
      text-align: center;
    }

    .footer {
      position: relative;
      
    }
    .logo {
      width: 125px;
      height: 125px;
      padding-top: 5px;
    }

    .marquee {
      color: black;
      font-size: 54px;
      font-weight: bold;
      margin-bottom: 20px;
      text-align: center;
    }

    .notmaltext {
      font-size: 1.1rem;
      text-align: center;
    }

    .course-title {
      font-weight: bold;
      margin-top: 2rem;
      font-size: 2rem;
      text-align: center;
    }

    .border {
      border-style: solid;
      border-width: 0.5px;
      border-color: gainsboro;
    }

    .person {
      font-size: 36px;
      margin: 10px auto;
      text-align: center;
    }

    .bottomimage {
      width: 80px;
      height: 80px;
    }

    .signature-wrapper {
      display: flex;
      justify-content: center;
      align-items: center;
    }

    .signatureimage {
      width: 80px;
      height: 80px;
      text-align: center;
    }
.item {
  /* Optional styling for the items */
  position: absolute;
  top: 50%; /* Center vertically */
  transform: translateY(-50%);
}

#item1 {
  left: 10%; /* Set the left position of Item 1 */
}

#item2 {
  left: 50%; /* Set the left position of Item 2 */
  transform: translateX(-50%) translateY(-50%); /* Center horizontally */
}

#item3 {
  right: 10%; /* Set the right position of Item 3 */
}


  </style>
  <div class="container">
    <div class="logo-wrapper">
      <img class="logo" src=https://storage.googleapis.com/calibr-assets/misc/Calibr-Logo.png />
    </div>
    <div class="wrapper">
      <div class="wrapper-content">
        <div class="marquee">Certificate of Completion</div>
        <div class="notmaltext">This is to certify that</div>

        <div class="person">{{name}}</div>
        <div class="notmaltext">
          has successfully completed the Online Course titled
        </div>

        <div class="course-title">{{course}}</div>
      </div>
    </div>
    <hr class="border" />

    <div class="footer">
      <div class="item" id="item1">
        <div>
          <div>{{date}}</div>
          <hr class="border" />
          <div>Date</div>
        </div>
      </div>
      <div class="item" id="item2">
        <img class="bottomimage" src=https://storage.googleapis.com/calibr-assets/misc/certificate_badge.png alt="logo">
      </div>
      <div class="item" id="item3">
        <div>
          <div class="signature-wrapper">
            <img class="signatureimage" src=https://storage.googleapis.com/calibr-assets/misc/calibr-signature.png
              alt="logo">
          </div>
          <hr class="border" />
          <div>Course Coordinator</div>
        </div>
      </div>
    </div>
  </div>
"""

    options = {
        'orientation': 'Landscape'
    }
    # Replace the placeholders
    html_content = html_content.replace("{{name}}", name)
    html_content = html_content.replace("{{course}}", course)
    html_content = html_content.replace("{{date}}", date)
    try:
        # Generate the certificate as a PDF file
        pdfkit.from_string(html_content, "certificate3.pdf", options=options)
        return "success"
    except Exception as e:
        # Handle the exception (failed to generate the PDF)

        return "failed"
