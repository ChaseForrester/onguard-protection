/** Schedule D — OG-LEG-2026-001 (post 1 June 2023). Do not invent subclasses. */
export const CLASS1 = {
    "1A": {
        code: "1A",
        label: "1A Security Officer (unarmed static/mobile + crowd controller – post-1 June 2023 merger)",
        authorises: [
            "static",
            "mobile_patrol",
            "alarm_response",
            "crowd_control",
            "event_security",
            "concierge",
            "construction_gate",
            "bag_search",
            "access_screening",
            "event_closeout",
        ],
        forbids: ["cash_in_transit", "dog_team", "armed", "bodyguard"],
    },
    "1B": {
        code: "1B",
        label: "1B Bodyguard",
        authorises: ["bodyguard"],
        forbids: ["cash_in_transit", "dog_team", "armed"],
    },
    "1C": {
        code: "1C",
        label: "1C Cash-in-Transit Guard",
        authorises: ["cash_in_transit"],
        forbids: ["dog_team"],
    },
    "1D": {
        code: "1D",
        label: "1D Guard Dog Handler",
        authorises: ["dog_team"],
        forbids: [],
    },
    "1E": {
        code: "1E",
        label: "1E Monitoring Centre Operator",
        authorises: ["monitoring_centre"],
        forbids: ["dog_team", "armed", "cash_in_transit"],
    },
    "1F": {
        code: "1F",
        label: "1F Armed Guard",
        authorises: ["armed"],
        forbids: ["dog_team"],
    },
} as const;

export type Class1Code = keyof typeof CLASS1;
export const CLASS1_CODES = Object.keys(CLASS1) as Class1Code[];

export type Activity =
    | "static"
    | "mobile_patrol"
    | "alarm_response"
    | "crowd_control"
    | "event_security"
    | "concierge"
    | "construction_gate"
    | "bag_search"
    | "access_screening"
    | "event_closeout"
    | "bodyguard"
    | "cash_in_transit"
    | "dog_team"
    | "monitoring_centre"
    | "armed";

export const NSW_ONLY = "NSW" as const;

/** Roster rule: every required activity must be authorised by at least one held subclass. */
export function rosterAllows(held: Class1Code[], required: Activity[]): boolean {
    if (!held.length || !required.length) return false;
    const auth = new Set<Activity>();
    for (const code of held) {
        const row = CLASS1[code];
        if (!row) return false;
        row.authorises.forEach((a) => auth.add(a));
    }
    return required.every((a) => auth.has(a));
}

/** 1A/1B/1C/1E/1F never authorise dog work. */
export function dogWorkLegal(held: Class1Code[]): boolean {
    return held.includes("1D");
}
