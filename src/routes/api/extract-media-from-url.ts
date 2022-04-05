import { createRequire } from 'module';
const require = createRequire(import.meta.url);
const puppeteer = require('puppeteer');

/** @type {RequestHandler} */
export async function post({ request }) {

  const { url } = await request.json();

  const browser = await puppeteer.launch({
    args: ['--no-sandbox', '--disable-setuid-sandbox'],
    headless: true,
  });

  const page = await browser.newPage();
  await page.goto(url);
  await page.waitForSelector('video');

  // get all video tags
  const videoTags = await page.$$eval('video', videos => videos.map(video => video.src));

  await browser.close();
  return {
    status: 200,
    body: {
      videoTags,
    }
  };
}