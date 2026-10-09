"""Voiceover lines for the concept-suite reels. Narrator voice (never first person "I" — the voice isn't Vatsal).
Each reel: hook (0.35–3.0 s), one line per caption window, end-card line (16.1–18.7 s), sting line (19.2–21.3 s).
Written for speech: no abbreviations the TTS would spell oddly."""

STING = "Waypoint Software."

VO = {
 "S00_suite-overview": dict(
  hook="Same address, typed into five apps. Or typed once.",
  caps=["Twelve apps. One customer record behind all of them.",
        "Dana books online. The crew's job and photos join her record.",
        "The invoice, the crew's hours, and Monday's numbers follow.",
        "Every app here is a concept. Yours gets only what you need."],
  end="A whole suite, built around how your business works."),
 "S01_clients-crm": dict(
  hook="One customer. Every call, quote and job, on one screen.",
  caps=["Every customer in one list. Search by name, street or phone.",
        "Calls, quotes, jobs and invoices, on one timeline.",
        "Add a note once, and the crew sees it on the job.",
        "Book the next visit from the same page."],
  end="A client list that knows the rest of your business."),
 "S02_schedule-booking": dict(
  hook="A fall cleanup request. Which crew is nearby Thursday?",
  caps=["Dana books a fall cleanup from the website.",
        "It lands in Sam's week view, beside every booking.",
        "Thursday fits. Owen's crew is already in Kentville.",
        "One tap confirms. Dana gets a text. The crew gets the job."],
  end="A schedule that knows where every crew is."),
 "S03_quotes-invoicing": dict(
  hook="Price the driveway. Get it signed. Match the payment.",
  caps=["Tap items from the price list. The tax adds itself.",
        "Send it as a link, and watch it flip to signed.",
        "One tap turns the signed quote into an invoice.",
        "An e-transfer comes in. Confirm the match. Paid."],
  end="Quotes that become invoices, from your own price list."),
 "S04_jobs-crew": dict(
  hook="The crew knows the gate code before the truck pulls in.",
  caps=["Today's jobs, in route order, on the crew lead's phone.",
        "The office note is pinned at the top.",
        "Tick the checklist. Add before and after photos.",
        "Mark it done. Hours are logged, and the invoice is drafted."],
  end="A crew app, built around how your jobs already run."),
 "S05_people-hr": dict(
  hook="New hire Monday. His paperwork comes from his own phone.",
  caps=["Theo starts Monday. His onboarding checklist is waiting.",
        "He fills in his tax forms and banking, on his phone.",
        "Boots and radio handed over? Erin ticks that one herself.",
        "Profile complete. Payroll picks Theo up from there."],
  end="Onboarding that follows your own checklist."),
 "S06_payroll": dict(
  hook="Two weeks of crew hours, checked before anyone is paid.",
  caps=["Hours come in from the job app, per crew member.",
        "Two flags: a missed clock-out, and overtime.",
        "Erin fixes the punch, and leaves a note on the record.",
        "Every deduction is listed. Nothing is paid until she approves."],
  end="Pay runs that follow your crew's real hours."),
 "S07_time-off": dict(
  hook="Maya wants two days off. Is snow-prep week covered?",
  caps=["Maya picks her days. Her balance shows as she goes.",
        "Erin sees the request next to the crew's week.",
        "The snow-prep day is flagged before she decides.",
        "Approved. The balance updates, and the schedule plans around her."],
  end="Time off that checks the schedule first."),
 "S08_helpdesk": dict(
  hook="The plow missed a driveway. The text reaches the right crew.",
  caps=["Texts, web forms and emails land in one inbox.",
        "Already linked to Tom's record, and last night's plow job.",
        "Assign it to Owen. Edit a saved reply. Send.",
        "When Owen marks the revisit done, it's resolved."],
  end="One inbox that already knows your clients."),
 "S09_stock-inventory": dict(
  hook="Every salted driveway comes off the ice melt count.",
  caps=["Everything in the yard, with what's on hand.",
        "Each salted driveway takes bags off the count.",
        "Below the reorder point, a purchase order is drafted.",
        "Nothing is ordered until Erin taps approve."],
  end="Stock counts that move with the crew's jobs."),
 "S10_campaigns-email": dict(
  hook="Who had a fall cleanup, but no snow contract yet?",
  caps=["Pick who gets it: fall cleanup, no winter contract.",
        "Only clients with consent on file. Everyone else is left out.",
        "Write it once. Each client sees their own first name.",
        "Schedule it for Tuesday morning. Replies come back to the helpdesk."],
  end="Email that starts from your own client list."),
 "S11_reports": dict(
  hook="Monday morning. Last week's jobs, invoices, and who still owes.",
  caps=["Last week's numbers are already filled in.",
        "Each number comes from the app where the work happened.",
        "Tap unpaid. Three invoices, oldest first.",
        "Reminders are drafted. Erin sends them herself."],
  end="Reports that read straight from the work you log."),
 "S12_ai-assistant": dict(
  hook="Ask who still owes you. Get names, not a dashboard.",
  caps=["Erin asks a plain question. No report to build.",
        "The answer comes from her own invoices, sources shown.",
        "She asks for reminders. The assistant only drafts them.",
        "Erin changes a word, and approves each one herself."],
  end="An assistant that drafts, and waits for your yes."),
}
